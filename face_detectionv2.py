import time
import mediapipe as mp
import cv2

class FaceMeshDetector:
    def __init__(self, max_faces=2): #ограничение в два лица на видео
        self.max_faces = max_faces
        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(max_num_faces=self.max_faces)
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=2)

    def findFaceMesh(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.faceMesh.process(imgRGB)
        faces = []
        if results.multi_face_landmarks:
            for faceLms in results.multi_face_landmarks:
                face = []
                for lm in faceLms.landmark:
                    ih, iw, ic = img.shape
                    x, y = int(lm.x * iw), int(lm.y * ih)
                    face.append((x, y))
                faces.append(face)
                self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACEMESH_CONTOURS, self.drawSpec, self.drawSpec)
        return img, faces

def main():
    print("Starting program...")  # Отладочный вывод
    cap = cv2.VideoCapture(0)  #  --->  0 это запуск веб-камеры
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    pTime = 0
    detector = FaceMeshDetector(max_faces=2)

    while True:
        success, img = cap.read()
        if not success:
            print("Error: Failed to read frame.")
            break

        img, faces = detector.findFaceMesh(img)

        if len(faces) != 0:
            print(faces[0])

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3) # Смена цвета индикации лицаб сейчас белый
        cv2.imshow('Image', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
