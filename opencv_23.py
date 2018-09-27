import cv2 as cv
import numpy as np

#  中值模糊
#
#  中值滤波本质上是统计排序滤波器的一种，中值滤波对图像特定噪声类型（椒盐噪声）会取得比较好的去噪效果，也是常见的图像去噪声与增强的方法之一。中值滤波也是窗口在图像上移动，其覆盖的对应ROI区域下，所有像素值排序，取中值作为中心像素点的输出值
#
#  OpenCV中值滤波API函数如下：
#  medianBlur	(
#  InputArray 	src,
#  OutputArray 	dst,
#  int 	ksize // 必须是奇数，而且必须大于1
#  )
#
#  Python:
#  dst = cv.medianBlur(	src, ksize[, dst]	)#

src = cv.imread("sp_noise.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

dst = cv.medianBlur(src, 5)
cv.imshow("blur ksize=5", dst)

cv.waitKey(0)
cv.destroyAllWindows()


