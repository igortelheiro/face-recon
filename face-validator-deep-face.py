import cv2
import os
import face_recognition
from deepface import DeepFace

# Função para carregar as imagens cadastradas e codificar as faces
def carregar_faces_cadastradas(directory):
    face_encodings = []
    for subdir, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".png"):
                image_path = os.path.join(subdir, file)
                face_encodings.append(image_path)
    return face_encodings

# Diretório onde as imagens cadastradas estão armazenadas
faces_cadastradas_dir = "coletas_faciais"
faces_cadastradas = carregar_faces_cadastradas(faces_cadastradas_dir)

# Inicializa a webcam
cap = cv2.VideoCapture(0)

while True:
    # Captura o quadro da webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Converte o quadro para RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Localiza todas as faces no quadro atual da webcam
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Verifica cada face encontrada no quadro
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        name = "Desconhecido"
        for face_path in faces_cadastradas:
            result = DeepFace.verify(rgb_frame[top:bottom, left:right], face_path, model_name='VGG-Face', enforce_detection=False)
            if result["verified"]:
                name = "Cadastrado"
                break

        # Desenha um retângulo ao redor da face e exibe se está cadastrado ou não
        color = (0, 255, 0) if name == "Cadastrado" else (0, 0, 255)
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    # Exibe o quadro com as verificações
    cv2.imshow("Verificação de Rosto", frame)

    # Pressiona 'q' para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a câmera e fecha as janelas
cap.release()
cv2.destroyAllWindows()
