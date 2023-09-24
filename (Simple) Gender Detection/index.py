import cv2
import numpy as np
from keras.preprocessing import image
from keras.models import load_model

model_gender = load_model('model_gender.h5')

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

gender_labels = ['Male', 'Female']

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        face = frame[y:y + h, x:x + w]
        
        face = cv2.resize(face, (128, 128))
        face = image.img_to_array(face)
        face = np.expand_dims(face, axis=0)
        
        predicted_gender = model_gender.predict(face)
        gender = gender_labels[np.argmax(predicted_gender)]
        
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, gender, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow('Cek Kelamin', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
