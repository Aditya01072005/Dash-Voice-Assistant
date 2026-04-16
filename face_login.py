from deepface import DeepFace
import cv2
import subprocess
import sys

print("Face Login Started...")

cam = cv2.VideoCapture(0)
frame_count = 0

while True:
    ret, frame = cam.read()

    if not ret:
        print("Camera error")
        break

    # Always show camera smoothly
    display_frame = frame.copy()
    cv2.putText(display_frame, "Scanning...",
                (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2)

    cv2.imshow("Face Login", display_frame)

    # Only run DeepFace every 30 frames (~1 sec)
    frame_count += 1
    if frame_count % 30 == 0:

        cv2.imwrite("temp.jpg", frame)

        try:
            result = DeepFace.verify(
                img1_path="my_face.jpg",
                img2_path="temp.jpg",
                enforce_detection=False
            )

            print("Checking...")

            if result["verified"]:
                print("Access Granted")
                cam.release()
                cv2.destroyAllWindows()

                subprocess.run([sys.executable, "main.py"])
                break

        except Exception as e:
            print("Error:", e)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()