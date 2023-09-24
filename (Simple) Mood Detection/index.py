import cv2
from keras.models import load_model
import numpy as np

model = load_model('model_filter.h5')

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

emotion_labels = ['Marah', 'Menjijikan / Aneh', 'Takut', 'Senang', 'Sedih', 'Surprise / Kaget', 'Datar']

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        face = gray[y:y + h, x:x + w]

        face = cv2.resize(face, (48, 48))
        face = np.reshape(face, [1, 48, 48, 1])

        predicted_class = np.argmax(model.predict(face))
        label = emotion_labels[predicted_class]

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow('Deteksi Ekspresi', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
