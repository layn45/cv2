import cv2
import time
import mediapipe as mp
 
cap= cv2.VideoCapture(0)
pTime=0
mppose=mp.solutions.pose
mpdrawstyle=mp.solutions.drawing_styles
mpdraw=mp.solutions.drawing_utils
pose=mppose.Pose()

run=True

while run:
    success,img=cap.read()
    results=pose.process(img)
    
    if results.pose_landmarks:
        mpdraw.draw_landmarks(img,results.pose_landmarks,mppose.POSE_CONNECTIONS)
        for id,lm in enumerate(results.pose_landmarks.landmark):
            h,w,c=img.shape
            cx,cy=int(lm.x*w),int(lm.y*h)
            if id<=10:
                cv2.circle(img,(cx,cy),5,(0,0,255),5,cv2.FILLED)
            elif id<=22 and id>10:
                cv2.circle(img,(cx,cy),5,(0,255,0),5,cv2.FILLED)
            elif id<=32 and id>22:
                cv2.circle(img,(cx,cy),5,(255,0,0),5,cv2.FILLED)          
    ctime=time.time()
    fps=1/(ctime-pTime)
    pTime=ctime
    cv2.putText(img,f'fps:{str(int(fps))}',(20,70),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),3)
    
    
    
    cv2.imshow('holistic',img)
    key=cv2.waitKey(1)
    if key ==ord('q'):
        run =False
    