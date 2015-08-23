import cv2.cv as cv
import string
import sys, os
imagine = str(sys.argv[1])
im=cv.LoadImageM(imagine)
storage=cv.CreateMemStorage()
haar=cv.Load("/home/john/Downloads/opencv-2.4.5/data/haarcascades/haarcascade_frontalface_default.xml")
detected=cv.HaarDetectObjects(im, haar, storage, 1.1, 2, cv.CV_HAAR_DO_CANNY_PRUNING, (10,10))
i = 0
if detected:
     for face in detected:
             i=i+1
             xx = face[0][0]
             yy = face[0][1]
             width = face[0][2]
             height = face[0][3]
             pankaj12 = (width,height)
             cvIm = cv.LoadImage(imagine)
             cropped = cv.CreateImage(pankaj12,cvIm.depth, cvIm.nChannels)
             src_region = cv.GetSubRect(cvIm, face[0])
             cv.Copy(src_region, cropped)
             cv.SaveImage("Pankaj"+str(i)+".jpg",cropped)


