# import cv2
# import os
# from deepface import DeepFace
# import ffmpeg
# import sys

# # Configurações para DeepFace
# os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

# # Caminho do vídeo de entrada e de saída
# input_video_path = './input/teste1.mp4'
# processed_video_path = 'processed_video.avi'
# final_output_path = 'output_video3.mp4'

# # Abrir o vídeo de entrada
# cap = cv2.VideoCapture(input_video_path)

# # Verificar se o vídeo foi aberto corretamente
# if not cap.isOpened():
#     print("Error: Could not open video.")
#     sys.exit()

# # Obter FPS e dimensões do vídeo de entrada
# fps = int(cap.get(cv2.CAP_PROP_FPS))
# frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# # Criar o objeto VideoWriter para salvar o vídeo processado
# fourcc = cv2.VideoWriter_fourcc(*'MJPG')
# out = cv2.VideoWriter(processed_video_path, fourcc, fps, (frame_width, frame_height))
# idx = 0
# # Processar cada frame do vídeo
# while cap.isOpened():
#     idx += idx
#     print("index: ", idx)
    
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Detectar emoções no frame
#     try:
#         analysis = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

#         for result in analysis:
#             dominant_emotion = result['dominant_emotion']
#             emotion_score = result['emotion'][dominant_emotion]

#             # Obter coordenadas da face
#             region = result['region']
#             x, y, w, h = region['x'], region['y'], region['w'], region['h']

#             # Desenhar um retângulo ao redor da face
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

#             # Adicionar texto à imagem
#             cv2.putText(frame, f'{dominant_emotion}: {emotion_score:.2f}', 
#                         (x, y - 10), 
#                         cv2.FONT_HERSHEY_SIMPLEX, 
#                         0.5, (0, 0, 255), 2)
#     except Exception as e:
#         print(f'Error detecting emotions: {e}')

#     # Adicionar o frame processado ao vídeo de saída
#     out.write(frame)
    
# print("finish write frame!")    

# # Libere os recursos de leitura e gravação de vídeo
# cap.release()
# out.release()
# cv2.destroyAllWindows()

# # Verifique se o arquivo processado foi criado com sucesso
# if not os.path.exists(processed_video_path):
#     print("Error: Processed video was not created.")
#     sys.exit()

# # Remontar o vídeo final com o áudio original
# print("Combining processed video with audio...")
# try:
#     # Criação do comando ffmpeg
#     ffmpeg.input(processed_video_path).output(
#         input_video_path,  # Adicionar o vídeo original como entrada
#         final_output_path,
#         codec="copy",  # Copia o codec de vídeo para manter a qualidade
#         acodec="aac",  # Codec de áudio compatível
#         map='0:v',     # Mapear o vídeo processado
#         map='1:a'      # Mapear o áudio original do vídeo
#     ).run(overwrite_output=True)  # Permitir sobrescrita do arquivo de saída
    
#     print("Video processing completed successfully.")
# except ffmpeg.Error as e:
#     print(f"Error occurred while processing video: {e.stderr.decode()}")

import cv2
import os
from deepface import DeepFace
import ffmpeg
import sys

# Configurações para DeepFace
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

# Caminho do vídeo de entrada e de saída
input_video_path = './input/teste1.mp4'
processed_video_path = 'processed_video.avi'
final_output_path = 'output_video3.mp4'

# Abrir o vídeo de entrada
cap = cv2.VideoCapture(input_video_path)

# Verificar se o vídeo foi aberto corretamente
if not cap.isOpened():
    print("Error: Could not open video.")
    sys.exit()

# Obter FPS e dimensões do vídeo de entrada
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Criar o objeto VideoWriter para salvar o vídeo processado
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter(processed_video_path, fourcc, fps, (frame_width, frame_height))
idx = 0
# Processar cada frame do vídeo
while True:
    idx += idx
    print("index: ", idx)
    ret, frame = cap.read()
    if not ret:
        break

    # Detectar emoções no frame
    try:
        analysis = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

        for result in analysis:
            dominant_emotion = result['dominant_emotion']
            emotion_score = result['emotion'][dominant_emotion]

            # Obter coordenadas da face
            region = result['region']
            x, y, w, h = region['x'], region['y'], region['w'], region['h']

            # Desenhar um retângulo ao redor da face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Adicionar texto à imagem
            cv2.putText(frame, f'{dominant_emotion}: {emotion_score:.2f}', 
                        (x, y - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 
                        0.5, (0, 0, 255), 2)
    except Exception as e:
        print(f'Error detecting emotions: {e}')

    # Adicionar o frame processado ao vídeo de saída
    out.write(frame)
print("finish write frame!")
# Libere os recursos de leitura e gravação de vídeo
cap.release()
out.release()
cv2.destroyAllWindows()

# Verifique se o arquivo processado foi criado com sucesso
if not os.path.exists(processed_video_path):
    print("Error: Processed video was not created.")
    sys.exit()

# Remontar o vídeo final com o áudio original
print("Combining processed video with audio...")
try:
    # Extraindo áudio do vídeo original
    audio_path = 'extracted_audio.aac'
    ffmpeg.input(input_video_path).output(audio_path, acodec='aac', vn=True).run(overwrite_output=True)

    # Combinando vídeo processado e áudio original
    ffmpeg.input(processed_video_path).output(
        audio_path, 
        final_output_path,
        vcodec='libx264',  # Codec de vídeo para manter a qualidade
        acodec='aac',      # Codec de áudio compatível
        shortest=None      # Faz com que o resultado tenha a duração do vídeo mais curto
    ).run(overwrite_output=True)  # Permitir sobrescrita do arquivo de saída

    # Remover o arquivo de áudio extraído se não for mais necessário
    os.remove(audio_path)
    
    print("Video processing completed successfully.")
except ffmpeg.Error as e:
    print(f"Error occurred while processing video: {e.stderr.decode()}")
