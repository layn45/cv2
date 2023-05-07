import random
import cv2
import time
import mediapipe as mp
import cvzone
import numpy as np
from cvzone.HandTrackingModule import HandDetector
sec=[10]
cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)
start=0
detector = HandDetector(maxHands=1)
run=True
point=[0]
# sen = 30
text=random.randint(1,4)
if text==1:
    textList=['_']
    
if text==2:
    textList=['|']
if text==3:
    textList=['L']
if text==4:
    textList=['v']
pm=''
tt=0
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=3, min_detection_confidence=0.3, min_tracking_confidence=0.3)
mpDraw = mp.solutions.drawing_utils

while run:
    
    success, img = cap.read()
    imgText = np.zeros_like(img)
    results = hands.process(img) 
    if start==0:
        cv2.putText(imgText,'press "s" to start the game', (40,150), cv2.FONT_HERSHEY_TRIPLEX,1,(255,255,255),2)
        point=[0]


    hands1, img = detector.findHands(img)

    if sec[0]<1:
        start=3
        if results.multi_hand_landmarks:
            for i,txt in enumerate(point):
                txt=str(txt)
                cv2.putText(imgText,txt,(270,340),cv2.FONT_HERSHEY_TRIPLEX,5,(255,255,255),5)
    if start == 2: 
        sec[0]-=1
        time.sleep(1)
        if hands1:
            playerMove = None
            hand = hands1[0]
            fingers = detector.fingersUp(hand)
            # cv2.putText(img,textlist, (100,100), cv2.FONT_HERSHEY_TRIPLEX, 55,(255,255,255),2)
            if fingers == [0,0,0,0,0]:
                start= False
            if fingers == [1, 0, 0, 0, 0]:
                playerMove = 1

            if fingers == [0, 1, 0, 0, 0]:
                playerMove = 2

            if fingers == [1, 1, 0, 0, 0]:
                playerMove = 3

            if fingers == [0, 1, 1, 0, 0]:
                playerMove = 4

            if playerMove == 1:
                print("_")
                pm='_'

            if playerMove == 2:
                print("|")
                pm='|'
            if playerMove == 3:
                print("L")
                pm='L'
            if playerMove == 4:
                print("v")
                pm='v'    
            if results.multi_hand_landmarks:
                for i, text in enumerate(textList):
                    cv2.putText(imgText, text, (270, 340),
                                cv2.FONT_HERSHEY_TRIPLEX, 5, (255, 255, 255), 2)
            if results.multi_hand_landmarks:
                for i,txt in enumerate(point):
                    txt=str(txt)
                    cv2.putText(imgText,txt,(70,100),cv2.FONT_HERSHEY_DUPLEX,2,(255,255,255),2)
            if results.multi_hand_landmarks:
                for i,tx in enumerate(sec):
                    tx=str(tx)
                    cv2.putText(imgText,tx,(270,100),cv2.FONT_HERSHEY_DUPLEX,2,(255,255,255),2)
            if pm==textList[0]:
                point[0]+=1
                while text != tt:
                    text=random.randint(1,4)
                    if text==1:
                        textList=['_']
                        tt=1
                    if text==2:
                        textList=['|']
                        tt=2
                    if text==3:
                        textList=['L']
                        tt=3
                    if text==4:
                        textList=['v']
                        tt=4

    imgstack=cvzone.stackImages([img,imgText],2,1)
    cv2.imshow('project',imgstack)
    key=cv2.waitKey(1)


    if key == ord('s'):
        start = 2   
    if key == ord('q'):
        run = False   