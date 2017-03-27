from subprocess import call
import cv2
import time

def backlight(value):
    call("xbacklight -set %d"%(value),shell=True)
vc = cv2.VideoCapture(0)

while True:
    rval,frame=vc.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    total,_,_,_=cv2.sumElems(gray)
    avg=total/(640*480)
    print avg
    xyz=avg
    if avg>250:
        backlight(80)
    elif avg>200:
        backlight(50)
    elif avg>100:
        backlight(35)
    elif avg>50:
        backlight(25)
    else:
        backlight(15)
    print "Setting brightness value"
    key = cv2.waitKey(500)
    if key==1048603:
        break

