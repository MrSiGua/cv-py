# 边缘保留滤波算法 – 均值迁移模糊(mean-shift blur)
# 均值迁移模糊是图像边缘保留滤波算法中一种，经常用来在对图像进行分水岭分割之前去噪声，可以大幅度提升分水岭分割的效果。均值迁移模糊的主要思想如下：
# 就是在图像进行开窗的时候同样，考虑像素值空间范围分布，只有符合分布的像素点才参与计算，计算得到像素均值与空间位置均值，
# 使用新的均值位置作为窗口中心位置继续基于给定像素值空间分布计算均值与均值位置，如此不断迁移中心位置直到不再变化位置（dx=dy=0），
# 但是在实际情况中我们会人为设置一个停止条件比如迁移几次，这样就可以把最后的RGB均值赋值给中心位置。
#
# OpenCV中均值迁移滤波的API函数：
# C++:
# pyrMeanShiftFiltering(
# InputArray 	src,
# OutputArray 	dst,
# double 	sp,
# double 	sr,
# int 	maxLevel = 1,
# TermCriteria  termcrit =
# TermCriteria(TermCriteria::MAX_ITER+TermCriteria::EPS, 5, 1)
# )
# Python:
# dst=cv.pyrMeanShiftFiltering(	src, sp, sr[, dst[, maxLevel[, termcrit]]])


import cv2 as cv
import numpy as np

src = cv.imread("example.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

h, w = src.shape[:2]
dst = cv.pyrMeanShiftFiltering(src, 15, 30, termcrit=(cv.TERM_CRITERIA_MAX_ITER+cv.TERM_CRITERIA_EPS, 5, 1))
result = np.zeros([h, w*2, 3], dtype=src.dtype)
result[0:h,0:w,:] = src
result[0:h,w:2*w,:] = dst
cv.imshow("result", result)
cv.imwrite("D:/result.png", result)


cv.waitKey(0)
cv.destroyAllWindows()
