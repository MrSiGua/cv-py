# 边缘保留滤波算法 – 高斯双边模糊
# 前面我们介绍的图像卷积处理无论是均值还是高斯都是属于模糊卷积，
# 它们都有一个共同的特点就是模糊之后图像的边缘信息不复存在，受到了破坏。
# 我们今天介绍的滤波方法有能力通过卷积处理实现图像模糊的同时对图像边缘不会造成破坏，滤波之后的输出完整的保存了图像整体边缘（轮廓）信息，
# 我们称这类滤波算法为边缘保留滤波算法（EPF）。最常见的边缘保留滤波算法有以下几种
# -	高斯双边模糊
# -	Meanshift均值迁移模糊
# -	局部均方差模糊
# -	OpenCV中对边缘保留滤波还有一个专门的API
# 本周我们的分享就从最经典的高斯双边模糊开始，高斯模糊是考虑图像空间位置对权重的影响，但是它没有考虑图像像素分布对图像卷积输出的影响，
# 双边模糊考虑了像素值分布的影响，对像素值空间分布差异较大的进行保留从而完整的保留了图像的边缘信息。
# C++:
# bilateralFilter(
# InputArray 	src,
# OutputArray 	dst,
# int 	d,
# double 	sigmaColor,
# double 	sigmaSpace,
# int 	borderType = BORDER_DEFAULT
# )
# Python:
# dst	=	cv.bilateralFilter(	src, d, sigmaColor, sigmaSpace[, dst[, borderType]]	)#

# 双边模糊考虑了像素值分布的影响，对像素值空间分布差异较大的进行保留从而完整的保留了图像的边缘信息。
# EPF


import cv2 as cv
import numpy as np

src = cv.imread("example.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

h, w = src.shape[:2]
dst = cv.bilateralFilter(src, 0, 100, 10)
result = np.zeros([h, w*2, 3], dtype=src.dtype)
result[0:h, 0:w, :] = src
result[0:h, w:2*w, :] = dst
cv.imshow("result", result)


cv.waitKey(0)
cv.destroyAllWindows()
