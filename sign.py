#This code demonstrate how to show location of hand landmark
import cv2
import mediapipe as mp
myname = 'NUY'
Nfing = 5
cap = cv2.VideoCapture(0)

#Call hand pipe line module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 4:
                    id4 = int(id)
                    cx4 = cx
                if id == 3:
                    id3 = int(id)
                    cx3 = cx
                if id == 2:
                    id2 = int(id)
                    cx2 = cx  
                if id == 1:
                    id1 = int(id)
                    cx1 = cx
                 if id == 0:
                    id0 = int(id)
                    cx0 = cx    
            if  cx1 > cx0:
                Nfing = 1         
            elif cx2 > cx1:
                Nfing = 2          
            elif cx3 > cx2:
                Nfing = 3        
            elif cx4 > cx3:
                Nfing = 4
            else:
                Nfing = 5
      
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.putText(img, str(int(Nfing)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)
    cv2.putText(img, str(str(myname)), (500, 450), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
#Closeing all open windows
#cv2.destroyAllWindows()