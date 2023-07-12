import cv2
import mediapipe as mp
import time

# Gets video data from webcam 
cap = cv2.VideoCapture(0)

# Setting object using Hands class
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=4)
mpDraw = mp.solutions.drawing_utils

# Previous time / Current time variables for FPS calc
pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
 
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # Gets the specific ID and (x,y) Cords,
            for id, lm in enumerate(handLms.landmark):
                print(id,lm)
                h, w, c, = img.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
                print(id,cx,cy)
                # Draw circles on specific points specified in the below list
                # ids_to_draw = [4, 8, 12, 16, 20]
                # if id in ids_to_draw:
                #     cv2.circle(img,(cx,cy), 15, (255,255,0), cv2.FILLED)


            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, "FPS: " + str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,255), 3)
    cv2.imshow("image", img)
    cv2.waitKey(1)



