import cv2
import os
from fer import FER
import ffmpeg

# Configurações para FER
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
detector = FER()

# Caminho do vídeo de entrada e de saída
input_video_path = './input/video3.mp4'
processed_video_path = 'processed_video.avi'
final_output_path = 'output_video3.mp4'

# Abrir o vídeo de entrada
cap = cv2.VideoCapture(input_video_path)

# Obter FPS e dimensões do vídeo de entrada
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Criar o objeto VideoWriter para salvar o vídeo processado
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter(processed_video_path, fourcc, fps, (frame_width, frame_height))

# Processar cada frame do vídeo
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Detectar emoções no frame
    result = detector.detect_emotions(frame)

    for face in result:
        box = face['box']
        emotions = face['emotions']
        
        # Obter as coordenadas do box
        x, y, w, h = box
        
        # Desenhar um retângulo ao redor da face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Determinar a emoção com a maior probabilidade
        emotion = max(emotions, key=emotions.get)
        
        # Adicionar texto à imagem
        cv2.putText(frame, f'{emotion}: {emotions[emotion]:.2f}', 
                    (x, y - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    0.5, (0, 0, 255), 2)

    # Adicionar o frame processado ao vídeo de saída
    out.write(frame)

# Libere os recursos de leitura e gravação de vídeo
cap.release()
out.release()
cv2.destroyAllWindows()

# Remontar o vídeo final com o áudio original
# Combinando o vídeo processado com o áudio original do vídeo de entrada usando ffmpeg
(
    ffmpeg
    .input(processed_video_path)
    .output(
        final_output_path,
        codec="copy",  # Copia o codec de vídeo para manter a qualidade
        acodec="aac",  # Codec de áudio compatível
        **{'map': '0:v:0'},  # Mapear o vídeo
        **{'map': '1:a:0'}   # Mapear o áudio original do vídeo
    )
    .run()
)
