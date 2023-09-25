import cv2
import numpy as np

net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

with open("coco.names", "r") as f:
    classes = f.read().strip().split("\n")

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

confidence_threshold = 0.2
nms_threshold = 0.4

while True:
    ret, frame = cap.read()

    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)

    net.setInput(blob)

    detections = net.forward()

    num_people = 0

    for detection in detections:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]

        if classes[class_id] == "person" and confidence > confidence_threshold:
            num_people += 1
            center_x, center_y, width, height = (detection[0:4] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])).astype('int')
            x, y = int(center_x - width / 2), int(center_y - height / 2)
            cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)

    cv2.putText(frame, f'Jumlah Orang: {num_people}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Deteksi Jumlah Orang', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
