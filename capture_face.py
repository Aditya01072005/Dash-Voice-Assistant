import cv2

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    cv2.imshow("Capture Face - Press S", frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("my_face2.jpg", frame)
        print("Face saved!")
        break

cam.release()
cv2.destroyAllWindows()