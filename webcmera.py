import cv2
import mediapipe as mp
web = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawings = mp.solutions.drawing_utils
hands=mp_hands.Hands()


while True:
    success,frame = web.read()
    if success == False:
        break
    rgb_img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    
    
   
    
   
    
    result = hands.process(rgb_img)
    print(result.multi_hand_landmarks)

    if result.multi_hand_landmarks:
        for hands_no, hand_land_marks in enumerate(result.multi_hand_landmarks):
            mp_drawings.draw_landmarks(image = frame,landmark_list = hand_land_marks,connections = mp_hands.HAND_CONNECTIONS)
    
    cv2.imshow("show",frame)
    if cv2.waitKey(2) & 0xFF==27:
        break

web.release()
cv2.destroyAllWindows()