import cv2 as cv
import numpy as np

src = cv.imread("lena.bmp")
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
cv.imshow("gray", gray)

minValue, maxValue, minLoc, maxLoc = cv.minMaxLoc(gray)
print("min: %.2f, max: %.2f" % (minValue, maxValue))
print("min loc:", minLoc)
print("max loc:", maxLoc)

means, stddev = cv.meanStdDev(gray)
print("mean: %.2f, stddev: %.2f" % (means, stddev))
gray[np.where(gray < means)] = 0
gray[np.where(gray > means)] = 255
cv.imshow("binary", gray)

cv.waitKey(0)
cv.destroyAllWindows()
