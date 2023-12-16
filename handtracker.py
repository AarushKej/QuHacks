import cv2
import mediapipe as mp
from mouse import Mouse
from _thread import start_new_thread
import face_recognition
import time

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
ms = Mouse()

known_image = face_recognition.load_image_file("WIN_20231216_11_38_35_Pro.jpg")
known_face_encoding = face_recognition.face_encodings(known_image)[0]

class Global():
    def __init__(self):
        self.face_locations = None

g = Global()

def fl():
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    while True:
        g.face_locations = face_recognition.face_locations(rgb_frame)
        if g.face_locations and g.face_locations[0][2]>0.9:
            time.sleep(30)

start_new_thread(fl, ())

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    results = hands.process(frame)
    finger_pos = {8: None, 16: None, 4: None, 12: None}
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = g.face_locations
    if face_locations and face_locations[0][2]>0.9:
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks: # working with each hand
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)

                    if id == 8 or id == 16 or id == 4 or id == 12:
                        finger_pos[id] = (cx, cy)
                        cv2.circle(frame, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
        try:
            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
            distance_index = ms.distanceBetweenFingers(finger_pos[4][0], finger_pos[8][0], finger_pos[4][1], finger_pos[8][1])
            distance_middle = ms.distanceBetweenFingers(finger_pos[4][0], finger_pos[12][0], finger_pos[4][1], finger_pos[12][1])
            distance_ring = ms.distanceBetweenFingers(finger_pos[4][0], finger_pos[16][0], finger_pos[4][1], finger_pos[16][1])
    
            start_new_thread(ms.updatePos, (finger_pos[4][0], finger_pos[4][1]))
            start_new_thread(ms.leftClick, (distance_index, finger_pos[4][0], finger_pos[4][1]))
            start_new_thread(ms.rightClick, (distance_ring, finger_pos[4][0], finger_pos[4][1]))
            start_new_thread(ms.drag, (distance_middle, finger_pos[4][0], finger_pos[4][1]))

        except:
            pass
    cv2.imshow("Output", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
