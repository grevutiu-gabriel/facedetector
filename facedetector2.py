import cv2

FACE_DETECT = "/usr/share/opencv/lbpcascades/lbpcascade_frontalface.xml"
EYE_DETECT = "/usr/share/opencv/haarcascades/haarcascade_eye.xml"
DOWNSCALE = 4
i=0

webcam = cv2.VideoCapture(0)
face_classifier = cv2.CascadeClassifier(FACE_DETECT)
eye_classifier = cv2.CascadeClassifier(EYE_DETECT)

if webcam.isOpened(): # try to get the first frame
    rval, frame = webcam.read()
else:
    rval = False

while rval:
    rval, frame = webcam.read()
    minisize = (frame.shape[1] / DOWNSCALE,frame.shape[0] / DOWNSCALE)
    miniframe = cv2.resize(frame, minisize)
    faces = face_classifier.detectMultiScale(miniframe)
    eyes = eye_classifier.detectMultiScale(miniframe)
    for f in faces:
        fx, fy, fw, fh = [fv * DOWNSCALE for fv in f]
        cv2.rectangle(frame, (fx, fy), (fx + fw, fy + fh), (0, 0, 255))
	cv2.imshow("cam", frame)
	i += 1;
	sub_face = miniframe[fy:fy+fh, fx:fx+fw]
	eyes = eye_classifier.detectMultiScale(sub_face)
        for (ex,ey, ew, eh) in eyes:
            cv2.rectangle(frame, (fx+ex,fy+ey), ((fx+ex+ew), (fy+ey+eh)), (50, 50, 50), 3)
            cv2.imshow('eyes = %s' % (eyes,), frame)

    cv2.imshow("cam", frame)

    rval, frame = webcam.read()

    key = cv2.waitKey(5)
    if key in [27, ord('Q'), ord('q')]: # exit on ESC
        break
