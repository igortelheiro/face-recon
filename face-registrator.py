import cv2
import os

# Função para criar uma pasta para a pessoa
def criar_pasta_pessoa(nome):
    directory = os.path.join("coletas_faciais", nome)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

# Solicita o nome ou ID da pessoa
nome_pessoa = input("Digite o nome ou ID da pessoa: ")
pasta_pessoa = criar_pasta_pessoa(nome_pessoa)

# Inicializa a webcam
cap = cv2.VideoCapture(0)

# Carrega o classificador de Haar para detecção facial
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

coleta_num = 0

while True:
    # Captura o quadro da webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Converte o quadro para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta faces no quadro
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Desenha retângulos ao redor das faces detectadas
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Salva a imagem da face na pasta da pessoa
        face_img = gray[y:y+h, x:x+w]
        coleta_num += 1
        cv2.imwrite(os.path.join(pasta_pessoa, f"face_{coleta_num}.png"), face_img)

    # Exibe o quadro com as detecções
    cv2.imshow("Coleta de Biometria Facial", frame)

    # Pressiona 'q' para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a câmera e fecha as janelas
cap.release()
cv2.destroyAllWindows()
