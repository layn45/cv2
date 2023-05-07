import mediapipe as mp
import cv2
import time

cap = cv2.VideoCapture(0)
stream = True

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=3, min_detection_confidence=0.3, min_tracking_confidence=0.3)
mpDraw = mp.solutions.drawing_utils

while stream:
    success, img = cap.read()
    results = hands.process(img)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                print(id, cx, cy)
                cv2.circle(img, (cx, cy), 10, (0, 255, 255), cv2.FILLED)


            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Hand Tracking", img)
    key = cv2.waitKey(1)

    if key == ord('q'):
        stream = False