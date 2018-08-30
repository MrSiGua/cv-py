import cv2 as cv
import numpy as np

src = cv.imread("lena.bmp")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

# X Flip 倒影
dst1 = cv.flip(src, 0)
cv.imshow("x-flip", dst1)

# Y Flip 倒影
dst2 = cv.flip(src, 1)
cv.imshow("Y-flip", dst2)

# XY Flip 对角
dst3 = cv.flip(src, -1)
cv.imshow("XY-flip", dst3)

# custom y-flip
h, w, ch = src.shape
dst = np.zeros(src.shape, src.dtype)
for row in range(h):
    for col in range(w):
        b, g, r = src[row, col]
        dst[row, w - col - 1] = [b, g, r]
cv.imshow("custom-y-flip", dst)

cv.waitKey(0)
cv.destroyAllWindows()
