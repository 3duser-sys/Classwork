import cv2
import time

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

VidCap = cv2.VideoCapture(0)

if not VidCap.isOpened():
    print("Error: Camera wasn't captured, try connecting one first...\nError Code: E001CAM")
    exit()

while True:
    ret, frame = VidCap.read()

    if not ret:
        print("Error: Could it be the camera? Couln't open it...\nError Code: E002RET")
        break
    
    print("Detecting your face...")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    time.sleep(1)

    print("Face succesfully Detected!")

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    cv2.imshow('Face Detection Started: Press q to quit', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

VidCap.release()
cv2.destroyAllWindows()
                      



    