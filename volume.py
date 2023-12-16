import cv2
import mediapipe as mp
import pyautogui
import face_recognition

x1, y1, x2, y2 = 0, 0, 0, 0



for id, landmark in enumerate(landmarks):
                    x = int(landmark.x * frame_width)
                    y = int(landmark.y * frame_height)
                    if id == 8:
                        x1 = x
                        y1 = y
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 0))
                    if id == 4:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 0))
                        x2 = x
                        y2 = y

            dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            volume_increment = dist // 4
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
            if volume_increment > 50:
                pyautogui.press("volumeup")
            else:
                pyautogui.press("volumedown")
