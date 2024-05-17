import mediapipe as mp
import cv2 
img1 = cv2.imread('/home/rizzal/Documents/git/Python/Hand Tracking/lp2.jpeg')

mp_hands = mp.solutions.hands
mp_drawings = mp.solutions.drawing_utils

rgb_img = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

hands = mp_hands.Hands(static_image_mode = True,max_num_hands = 2)

result = hands.process(rgb_img)
print(result.multi_handedness)
print(result.multi_hand_landmarks)


if result.multi_hand_landmarks:
    for hands_no, hand_land_marks in enumerate(result.multi_hand_landmarks):
        mp_drawings.draw_landmarks(image = img1,landmark_list = hand_land_marks,connections = mp_hands.HAND_CONNECTIONS)

cv2.imshow("Image",img1)
cv2.waitKey()
cv2.destroyAllWindows()