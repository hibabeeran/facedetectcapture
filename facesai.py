import cv2
import numpy as np
face_cascade= cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)
while True:
    try:
        check, frame = webcam.read()
        print(check) #prints true as long as the webcam is running
        print(frame) #prints matrix values of each framecd 
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces =face_cascade.detectMultiScale(gray,1.5,4)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if len(faces) > 0: 
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            print("Processing image...")
            print("Image saved!")
        if key == ord('q'):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
    except(KeyboardInterrupt):
        print("Program ended.")

