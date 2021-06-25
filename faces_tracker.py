import cv2 as cv

img = cv.imread('resources/messiandronaldo.jpeg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier("haar_faces.xml")

green = (000,255,0)

faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=6)

for (x,y,w,h) in faces:
    cv.rectangle(img, (x,y), (x+w,y+h), green, thickness=2)

cv.imshow('result', img)

cv.waitKey(0)