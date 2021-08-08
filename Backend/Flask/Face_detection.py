import cv2 as cv

img = cv.imread(r'C:\Users\ELCOT\Documents\Back-end\Flask\static\uploads\MARTHA.png')
cv.imshow("One Direction", img)
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# detection xml file
detect = cv.CascadeClassifier("face.xml")
face_detect = detect.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=19)
print(face_detect)


for (x, y, w, h) in face_detect:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 200, 0), thickness=2)
cv.imshow("Rectangel", img)
cv.waitKey(0)
