import cv2
import face_recognition
import numpy as np

# Load and process the reference image
imgElon = face_recognition.load_image_file("imageBasic/Elon Musk.JPG")
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
encodeElon = face_recognition.face_encodings(imgElon)[0]

# Load and process the test image with multiple faces
imgTest = face_recognition.load_image_file("imageBasic/Elon Group.jpg")
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

# Find all face locations and encodings in the test image
faceLocations = face_recognition.face_locations(imgTest)
faceEncodings = face_recognition.face_encodings(imgTest, faceLocations)

# Set a threshold for face similarity (lower means more similar)
threshold = 0.5  

# Loop through each detected face in the test image
for faceLoc, encodeFace in zip(faceLocations, faceEncodings):
    faceDist = face_recognition.face_distance([encodeElon], encodeFace)
    
    # If the face distance is below the threshold, consider it a match
    if faceDist[0] < threshold:
        cv2.rectangle(imgTest, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (0, 255, 0), 2)
        cv2.putText(imgTest, f'Match {round(faceDist[0], 2)}', (faceLoc[3], faceLoc[0] - 10), 
                    cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 0), 2)

# Function to resize image while maintaining aspect ratio
def resize_image(image, width=800):
    height, original_width = image.shape[:2]
    aspect_ratio = width / original_width
    new_height = int(height * aspect_ratio)
    return cv2.resize(image, (width, new_height))

# Resize images for display
resized_imgTest = resize_image(imgTest, 800)

# Show the results
cv2.imshow('Known Face - Yash Sawant', cv2.resize(imgElon, (300, 300)))
cv2.imshow('Test Image', resized_imgTest)
cv2.waitKey(0)
cv2.destroyAllWindows()
