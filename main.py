import cv2 as cv

img = cv.imread("images/img.jpg")
cv.imshow("Display window", img)
k = cv.waitKey(0)