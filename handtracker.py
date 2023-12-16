import cv2
import mediapipe as mp
from mouse import Mouse

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

ms = Mouse()

while True:
    ret, frame = cap.read()

    results = hands.process(frame)
    finger_pos = {8: None, 16: None, 4: None}
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks: # working with each hand
            for id, lm in enumerate(handLms.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                if id == 8 or id == 16 or id == 4:
                    finger_pos[id] = (cx, cy)
                    cv2.circle(frame, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
    try:
        mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
        distance_index = ms.distanceBetweenFingers(finger_pos[4][0], finger_pos[8][0], finger_pos[4][1], finger_pos[8][1])
        print(distance_index)
        ms.leftClick(distance_index)

    except:
        pass
    cv2.imshow("Output", frame)
    cv2.waitKey(1)