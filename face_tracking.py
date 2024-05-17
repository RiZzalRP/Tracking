import cv2
import mediapipe as mp

video = cv2.VideoCapture('/home/rizzal/Documents/git/Python/Opencv/mny.mp4')

mp_face= mp.solutions.face_mesh
mp_hand = mp.solutions.hands
mp_drawings = mp.solutions.drawing_utils
mp_drawing = mp.solutions.drawing_utils

face = mp_face.FaceMesh()
hand = mp_hand.Hands

while True:
    success,frame = video.read()

    result = face.process(frame)
    results = hand.process(frame)
    print(result.multi_face_landmarks)
    if result.multi_face_landmarks :
        for face_landmarks in result.multi_face_landmarks:
            mp_drawings.draw_landmarks(
                frame,
                face_landmarks,
                mp_face.FACEMESH_TESSELATION
            )
    if  results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawings.draw-face_landmarks(
                frame,
                result.hand_landmarks,
                mp_hand.HAND_CONNECTION

            )


    cv2.imshow("Face Tracking",frame)
    if cv2.waitKey(3) & 0xFF==27:
        break

video.release()
cv2.destroyAllWindows()