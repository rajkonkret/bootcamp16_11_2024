# pip install opencv-python
import cv2

image = cv2.imread("obraz.jpg")

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.005, minNeighbors=7, minSize=(60, 60))

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + w), (0, 255, 0), 2)

cv2.imshow("Detekcja twarzy", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
