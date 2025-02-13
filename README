# Face Recognition Project

This repository contains three main scripts for face registration and validation using the webcam. Below is a detailed explanation of each file and its functionalities.

## Files

### face-registrator.py
This script is used to register new faces. It captures images from the webcam, detects faces, and saves the images in a specific folder for each person.

- **Function `criar_pasta_pessoa(nome)`**: Creates a folder to store the person's images.
- **Main Loop**: Captures frames from the webcam, detects faces, draws rectangles around detected faces, and saves the face images in the person's folder.

### face-validator.py
This script is used to validate faces using the face_recognition library. It compares the faces captured by the webcam with the registered faces.

- **Function `carregar_faces_cadastradas(directory)`**: Loads and encodes the registered images.
- **Main Loop**: Captures frames from the webcam, detects faces, compares the faces with the registered ones, and draws rectangles around the faces indicating whether they are registered or not.

### face-validator-deep-face.py
This script is a variation of face-validator.py but uses the DeepFace library for face validation.

- **Function `carregar_faces_cadastradas(directory)`**: Loads the paths of the registered images.
- **Main Loop**: Captures frames from the webcam, detects faces, uses the DeepFace library to verify the faces, and draws rectangles around the faces indicating whether they are registered or not.

## How to Use

### Register Faces:
1. Run the script `face-registrator.py`.
2. Enter the person's name or ID when prompted.
3. The face images will be saved in the `coletas_faciais` folder.

### Validate Faces:
- For validation using face_recognition, run the script `face-validator.py`.
- For validation using DeepFace, run the script `face-validator-deep-face.py`.

The faces captured by the webcam will be compared with the registered faces, and it will be displayed whether the face is registered or not.

## Dependencies

- OpenCV
- face_recognition
- DeepFace (only for face-validator-deep-face.py)

Install the dependencies using:

```bash
pip install opencv-python face_recognition deepface
```

## Contribution

Feel free to contribute with improvements or new features. Fork the repository, create a branch for your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.