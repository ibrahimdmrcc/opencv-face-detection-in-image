import cv2

img = cv2.imread('kalabalik2.jpg.')

yuz_casc= cv2.CascadeClassifier('haarcascade-frontalface-default.xml')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

yuzler = yuz_casc.detectMultiScale(img_gray,1.1,4)

for (x,y,w,h) in yuzler:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow('yuzler',img)
cv2.waitKey(0)
cv2.destroyAllWindows()