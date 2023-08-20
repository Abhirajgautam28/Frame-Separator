import cv2
import os

cam = cv2.VideoCapture("sample.MP4")
try:
    if not os.path.exists('D:\GRAPHIC ERA\SEM 6\FRAME\OUTPUT'):
        os.makedirs('D:\GRAPHIC ERA\SEM 6\FRAME\OUTPUT')
except OSError:
    print('Error: Creating directory of data')
currentframe = 0
while (True):
    ret, frame = cam.read()
    if ret:
        name = 'D:\GRAPHIC ERA\SEM 6\FRAME\OUTPUT\Img' + str(currentframe) + '.jpg'
        print('Creating...' + name)
        cv2.imwrite(name, frame)
        currentframe += 1
        cam.set(1, currentframe)
    else:
        break
cam.release()
cv2.destroyAllWindows()
