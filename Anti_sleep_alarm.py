import numpy as np
import cv2
import os
from matplotlib import pyplot as plt
import pygame

pygame.init()

fast = cv2.FastFeatureDetector()

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False
i=0
xcount=0
while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    kp = fast.detect(frame,None)
    img2 = cv2.drawKeypoints(frame, kp, color=(255,0,0))
    print "Threshold: ", fast.getInt('threshold')
    print "nonmaxSuppression: ", fast.getBool('nonmaxSuppression')
    #print "neighborhood: ", fast.getInt('type')
    print "Total Keypoints with nonmaxSuppression: ", len(kp)
    #cv2.imwrite("image_%d.jpg"%(i),img2)
    if i==1 or i==0:
        base_points=len(kp)
        former=len(kp)
    fast.setBool('nonmaxSuppression',0)
    kp = fast.detect(frame,None)
    print "Total Keypoints without nonmaxSuppression: ", len(kp)
    img3 = cv2.drawKeypoints(frame, kp, color=(255,0,0))
    #cv2.imwrite("image1_%d.jpg"%(i),img3)
    if abs(len(kp)-former)<300:                    #THIS IS THE ACCURACY FACTOR, SET IT TO SOMEWHERE BETWEEN 150-400
        #print "ARE YOU SLEEPING??"
        xcount=xcount+1
    else:
        xcount=0
    print xcount
    if xcount==200:                               #THIS IS THE WAIT TIME
        pygame.mixer.music.load("alarm.wav")
        pygame.mixer.music.play()
        #os.system("shutdown now -h")
    if xcount==0:
        pygame.mixer.music.stop()
    key = cv2.waitKey(20)
    i=i+1
    former=len(kp)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("preview")
