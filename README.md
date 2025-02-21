# Face Recognition with OpenCV and Face_Recognition

This project implements face recognition using the `face_recognition` library and `OpenCV` to detect and match a known face in a test image containing multiple faces.

## Features
- Detects faces in an image using `face_recognition`
- Encodes and compares faces using `face_distance`
- Draws bounding boxes around matched faces
- Resizes images for better visualization


## How It Works
- The script loads and encodes the reference image.
- It then detects faces in the test image and encodes them.
- It compares the detected faces with the reference face using `face_distance`.
- If a match is found below the defined threshold (0.5), a green rectangle is drawn around the detected face.
- The results are displayed using OpenCV.


