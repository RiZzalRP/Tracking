import cv2 
import mediapipe as mp

mp_pose = mp.solutions.pose
mp_drawings = mp.solutions.drawing_utils

pose = mp_pose.Pose()

video = cv2.VideoCapture('/home/rizzal/Documents/git/Python/Opencv/mny.mp4')

while True:
    success,frame = video.read()
    if success == False:
        break

    rgb_img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result = pose.process(rgb_img)
    print(result.pose_landmarks)
    if result.pose_landmarks:
        mp_drawings.draw_landmarks(image = frame,landmark_list = result.pose_landmarks,connections = mp_pose.POSE_CONNECTIONS)





    cv2.imshow("Viddeoo body",frame)
    if cv2.waitKey(50) & 0xFF==27:
        break


video.release()
cv2.destroyAllWindows()