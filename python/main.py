import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject

cap = cv2.VideoCapture(0) 
detector = FaceDetector()  


arduino = SerialObject('COM5')

while True:
    success, img = cap.read() 
    img, bBoxes = detector.findFaces(img)  

    
    if len(bBoxes) > 0:
        arduino.sendData([1, 0])  # green LED 
    else:
        arduino.sendData([0, 1])  # red LED

    
    cv2.imshow("Video", img)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
