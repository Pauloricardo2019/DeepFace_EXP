# from fer import FER
# import cv2
# import os

# os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
# # Carregar a imagem processada
# img = cv2.imread('bent.jpeg')

# # Criar um detector de emoções
# detector = FER()

# # Detectar emoções
# result = detector.detect_emotions(img)

# print(result)

# for face in result:
#     box = face['box']
#     emotions = face['emotions']
    
#     # Obter as coordenadas do box
#     x, y, w, h = box
    
#     # Desenhar um retângulo ao redor da face
#     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
#     # Determinar a emoção com a maior probabilidade
#     emotion = max(emotions, key=emotions.get)
    
#     # Adicionar texto à imagem
#     cv2.putText(img, f'{emotion}: {emotions[emotion]:.2f}', 
#                 (x, y - 10), 
#                 cv2.FONT_HERSHEY_SIMPLEX, 
#                 0.5, (0, 0, 255), 2)

# # Salvar ou exibir a imagem
# cv2.imwrite('imagem_com_emocoes_bent.jpeg', img)
# cv2.imshow('Emoções Detectadas', img)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# # Exibir o resultado
# exit

# import cv2
# import os
# from fer import FER

# # Configurações
# video_path = './input_video/video.mp4'  # Caminho do vídeo de entrada
# output_video_path = 'output_video.avi'  # Caminho do vídeo de saída
# # fps = 30  # Frames por segundo do vídeo de saída

# # Crie um detector de emoções
# detector = FER()

# # Abrir o vídeo
# cap = cv2.VideoCapture(video_path)

# fps = cap.get(cv2.CAP_PROP_FPS)  # Usar o FPS do vídeo original


# # Obter as dimensões do vídeo
# frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# # Criar o objeto VideoWriter
# # fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec para MP4
# fourcc = cv2.VideoWriter_fourcc(*'MJPG')
# out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

# while True:
#     ret, frame = cap.read()  # Ler o frame
#     if not ret:
#         break  # Se não houver mais frames, sair do loop

#     # Detectar emoções
#     result = detector.detect_emotions(frame)

#     for face in result:
#         box = face['box']
#         emotions = face['emotions']
        
#         # Obter as coordenadas do box
#         x, y, w, h = box
        
#         # Desenhar um retângulo ao redor da face
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
#         # Determinar a emoção com a maior probabilidade
#         emotion = max(emotions, key=emotions.get)
        
#         # Adicionar texto à imagem
#         cv2.putText(frame, f'{emotion}: {emotions[emotion]:.2f}', 
#                     (x, y - 10), 
#                     cv2.FONT_HERSHEY_SIMPLEX, 
#                     0.5, (0, 0, 255), 2)

#     # Escrever o frame processado no vídeo de saída
#     out.write(frame)

# # Libere os recursos
# cap.release()
# out.release()
# cv2.destroyAllWindows()
import cv2
import os
from fer import FER

# Configuração para não usar GPU (se houver)
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

# Criar um detector de emoções
detector = FER()

# Abrir a webcam (0 para webcam padrão)
cap = cv2.VideoCapture(0)

# Configuração do vídeo de saída com FPS reduzido
output_video_path = 'output_emotions_video2.avi'
fps = 15  # Frames por segundo do vídeo de saída (reduzido para diminuir a velocidade)

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

    # Mostrar o frame processado com as emoções na tela
    # cv2.imshow('Emoções Detectadas', frame)

    # Adicionar o frame processado ao vídeo de saída
    out.write(frame)

    # Parar a captura ao pressionar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libere os recursos
cap.release()
out.release()
cv2.destroyAllWindows()
