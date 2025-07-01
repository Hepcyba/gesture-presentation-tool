import cv2
import mediapipe as mp
import pyautogui

prev_x = 0

def detect_swipe(lm_list):
    global prev_x
    curr_x = lm_list[8][0]  # x-coordinate of index finger tip
    diff = curr_x - prev_x
    prev_x = curr_x

    if diff > 40:
        return "swipe_right"
    elif diff < -40:
        return "swipe_left"
    return None

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

            lm_list = []
            for id, lm in enumerate(handLms.landmark):
                h, w, c = frame.shape
                lm_list.append((int(lm.x * w), int(lm.y * h)))

            if lm_list:
                gesture = detect_swipe(lm_list)
                if gesture == "swipe_right":
                    print("👉 Next Slide")
                    pyautogui.press('right')
                elif gesture == "swipe_left":
                    print("👈 Previous Slide")
                    pyautogui.press('left')

    cv2.imshow("Hand Tracker", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

