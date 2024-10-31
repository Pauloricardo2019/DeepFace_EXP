from deepface import DeepFace
import cv2
import os

# Configuração para não usar GPU (se houver)
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

# Abrir a webcam (0 para webcam padrão)
cap = cv2.VideoCapture(0)

# Configuração do vídeo de saída com FPS reduzido
output_video_path = 'output_emotions_video_deepface.avi'
fps = 10  # Frames por segundo do vídeo de saída (reduzido para diminuir a velocidade)

# Obter dimensões do vídeo
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Criar o objeto VideoWriter para salvar o vídeo
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()  # Ler o frame da webcam
    if not ret:
        break  # Se não houver mais frames, sair do loop

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

    # Mostrar o frame processado com as emoções na tela
    # cv2.imshow('Emoções Detectadas', frame)

    # Parar a captura ao pressionar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libere os recursos
cap.release()
out.release()
cv2.destroyAllWindows()
