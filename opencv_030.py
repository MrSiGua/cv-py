# OpenCV中的自定义滤波器
#
# 图像卷积最主要功能有图像模糊、锐化、梯度边缘等，前面已经分享图像卷积模糊的相关知识点，
# OpenCV除了支持上述的卷积模糊（均值与边缘保留）还支持自定义卷积核，实现自定义的滤波操作。
# 自定义卷积核常见的主要是均值、锐化、梯度等算子。下面的三个自定义卷积核分别可以实现卷积的均值模糊、锐化、梯度功能。
#
# 1，	1， 1      0， -1， 0        1， 0
# 1，	1， 1     -1，  5，-1        0  -1
# 1，	1， 1      0， -1， 0
#
# OpenCV自定义滤波器API:
# void cv::filter2D(
# InputArray src,
# OutputArray dst,
# int ddepth, // 默认-1
# InputArray kernel, // 卷积核或者卷积窗口大小
# Point anchor = Point(-1,-1),
# double delta = 0,
# int borderType = BORDER_DEFAULT
# )
# Python:
# dst=cv.filter2D(src, ddepth, kernel[, dst[, anchor[, delta[, borderType]]]]	)
#
# int ddepth, // 默认-1，表示输入与输出图像类型一致，但是当涉及浮点数计算时候，需要设置为CV_32F。滤波完成之后需要使用convertScaleAbs函数将结果转换为字节类型。#


import cv2 as cv
import numpy as np

src = cv.imread("test.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

blur_op = np.ones([5, 5], dtype=np.float32)/25.
shape_op = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]], np.float32)
grad_op = np.array([[1, 0],[0, -1]], dtype=np.float32)

dst1 = cv.filter2D(src, -1, blur_op)
dst2 = cv.filter2D(src, -1, shape_op)
dst3 = cv.filter2D(src, cv.CV_32F, grad_op)
dst3 = cv.convertScaleAbs(dst3)

cv.imshow("blur=5x5", dst1);
cv.imshow("shape=3x3", dst2);
cv.imshow("gradient=2x2", dst3);

cv.waitKey(0)
cv.destroyAllWindows()

