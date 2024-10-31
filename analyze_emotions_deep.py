# from deepface import DeepFace
# import cv2

# # Carregar a imagem
# img_path = 'bent.jpeg'  # Substitua pelo caminho da sua imagem
# img = cv2.imread(img_path)

# # Detectar emoções
# analysis = DeepFace.analyze(img_path, actions=['emotion'])

# # Exibir resultados
# dominant_emotion = analysis[0]['dominant_emotion']
# emotion_score = analysis[0]['emotion'][dominant_emotion]

# # Exibir resultados
# print(f'Dominant Emotion: {dominant_emotion}')
# print(analysis)  # Exibe todas as emoções detectadas e suas intensidades

# # Adicionar a emoção dominante à imagem
# cv2.putText(img, f'{dominant_emotion}: {emotion_score:.2f}', 
#             (50, 50),  # Posição do texto na imagem
#             cv2.FONT_HERSHEY_SIMPLEX, 
#             1,  # Tamanho do texto
#             (255, 0, 0),  # Cor do texto (azul)
#             2,  # Espessura do texto
#             cv2.LINE_AA)

# # Salvar a nova imagem
# output_path = 'bent_with_emotion.jpg'
# cv2.imwrite(output_path, img)

# # Exibir a imagem resultante
# cv2.imshow('Emotion Detected', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

from deepface import DeepFace
import cv2
import os

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

# Carregar a imagem
img_path = 'paulo_test.jpeg'  # Substitua pelo caminho da sua imagem
img = cv2.imread(img_path)

# Detectar emoções
analysis = DeepFace.analyze(img_path, actions=['emotion'])

# Exibir resultados
for result in analysis:
    dominant_emotion = result['dominant_emotion']
    emotion_score = result['emotion'][dominant_emotion]

    # Obter coordenadas da face
    region = result['region']
    x, y, w, h = region['x'], region['y'], region['w'], region['h']
    
    # Desenhar um retângulo ao redor da face
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Posicionar o texto da emoção ao lado do retângulo
    text_x = x + w + 10  # Um pequeno espaço à direita do retângulo
    text_y = y + h // 2  # Verticalmente centralizado em relação ao rosto

    # Adicionar a emoção dominante à imagem
    cv2.putText(img, f'{dominant_emotion}: {emotion_score:.2f}', 
                (text_x, text_y),  # Posição do texto
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.7,  # Tamanho do texto
                (255, 0, 0),  # Cor do texto (azul)
                2,  # Espessura do texto
                cv2.LINE_AA)

# Salvar a nova imagem
output_path = 'bent_with_emotion.jpg'
cv2.imwrite(output_path, img)

# Exibir a imagem resultante
cv2.imshow('Emotion Detected', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



