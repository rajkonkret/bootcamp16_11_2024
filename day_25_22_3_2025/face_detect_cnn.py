import cv2
import dlib
import matplotlib.pyplot as plt

# model sieci wytrenowany
cnn_model_path = "mmod_human_face_detector.dat"

image_path = "obraz.jpg"
image = cv2.imread(image_path)

if image is None:
    raise ValueError("Nie udało się wczytać obrazu")

rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

cnn_detector = dlib.cnn_face_detection_model_v1(cnn_model_path)

detections = cnn_detector(rgb_image, upsample_num_times=1)

for d in detections:
    rect = d.rect
    x, y, w, h = rect.left(), rect.top(), rect.width(), rect.height()
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

plt.figure(figsize=(10, 2))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title(f"Dokłądniejszy model - wykryto twarzy: {len(detections)}")
plt.axis("off")
plt.show()
