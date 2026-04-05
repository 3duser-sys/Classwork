import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

VidCap = cv2.VideoCapture(0)

if not VidCap.isOpened():
    print("Error: Camera wasn't captured, try connecting one first...\nError Code: E001CAM")
    exit()

mode = 2

while True:
    ret, frame = VidCap.read()

    if not ret:
        print("Error: Could it be the camera? Couln't open it...\nError Code: E002RET")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if mode == 1:
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(50, 50))
    else:
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, f'Ppl Count: {len(faces)} Mode: {mode}', (10, 30), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow('Face Tracking AND FACE COUNTING!!!!', frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('1'):
        mode = 1
    elif key == ord('2'):
        mode = 2

VidCap.release()
cv2.destroyAllWindows()