import mediapipe as mp
import cv2
import time
import cvzone
cap = cv2.VideoCapture(0)
pTime = 0

mpFaceMesh = mp.solutions.face_mesh
mpDraw = mp.solutions.drawing_utils
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=1, refine_landmarks=True)
drawingSpec = mpDraw.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=2)

run = True

while run:
    success, img = cap.read()
    results = faceMesh.process(img)
    # print(results)
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACEMESH_CONTOURS,
                                  drawingSpec, drawingSpec)

            for id, lm in enumerate(faceLms.landmark):
                ih, iw, ic = img.shape
                x, y = int(lm.x * iw), int(lm.y * ih)
                print("id: "+ str(id), end=' ')
                print("x: " + str(x), end=' ')
                print("y: "+ str(y))

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS:{str(int(fps))}', (20, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (0, 255, 0), 3)

    cv2.imshow("Face Mesh", img)
    key = cv2.waitKey(1)

    if key == ord('q'):
        run = False