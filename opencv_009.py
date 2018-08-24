import cv2 as cv

src = cv.imread("lena.bmp")
cv.namedWindow("rgb", cv.WINDOW_AUTOSIZE)
cv.imshow("rgb", src)

#RGB to HSV
hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

#RGB to YUV
yuv = cv.cvtColor(src, cv.COLOR_BGR2YUV)
cv.imshow('yuv', yuv)

#RGB to YCRCB
ycrcb = cv.cvtColor(src, cv.COLOR_BGR2YCrCb)
cv.imshow('ycrcb', ycrcb)

mask = cv.inRange(hsv, (35, 43, 46), (99, 255, 255))
cv.imshow('mask', mask)

cv.waitKey(0)
cv.destroyAllWindows()
