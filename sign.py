#This code demonstrate how to show location of hand landmark
import cv2
import mediapipe as mp
myname = 'NUY'
Nfing = 0
cap = cv2.VideoCapture(0)

#Call hand pipe line module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    Finger = [] #list string python
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            Nfing = 0
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 4:
                    id4 = int(id)
                    cx4 = cx
                if id == 3:
                    id3 = int(id)
                    cx3 = cx
                if id == 7:
                    id7 = int(id)
                    cy7 = cy
                if id == 8:
                    id8 = int(id)
                    cy8 = cy
                if id == 12:
                    id12 = int(id)
                    cy12 = cy
                if id == 10:
                    id10 = int(id)
                    cy10 = cy
                if id == 16:
                    id16 = int(id)
                    cy16 = cy
                if id == 14:
                    id14 = int(id)
                    cy14 = cy
                if id == 20:
                    id20 = int(id)
                    cy20 = cy
                if id == 18:
                    id18 = int(id)
                    cy18 = cy   
            if cx3 < cx4:
                Nfing += 1
                Finger.append ('Thumb')
            if cy8 < cy7:
                Nfing += 1
                Finger.append ('Index')
            if cy12 < cy10:
                Nfing += 1
                Finger.append ('Middle')
            if cy16 < cy14:
                Nfing += 1
                Finger.append ('Ring')
            if cy20 < cy18:
                Nfing += 1
                Finger.append ('Pinky')
      
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.putText(img, str(int(Nfing)), (20, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)
    cv2.putText(img, str(str(myname)), (500, 450), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)
    cv2.putText(img, str(str(Finger)), (50, 400), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
#Closeing all open windows
#cv2.destroyAllWindows()