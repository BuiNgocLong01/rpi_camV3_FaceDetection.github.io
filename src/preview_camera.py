
from picamera2 import Picamera2
import cv2

piCam = Picamera2()

piCam.preview_configuration.main.size=(1280,720)
piCam.preview_configuration.main.format='RGB888'
piCam.preview_configuration.main.align()
piCam.configure('preview')
piCam.start()

while True:
    frame = piCam.capture_array()
    frame = cv2.flip(frame, 1)
    cv2.imshow('piCam', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()