import cv2 as cv
import numpy as np

#  均值模糊 是卷积核的系数完全一致，高斯模糊考虑了中心像素距离的影响，对距离中心像素使用高斯分布公式生成不同的权重系数给卷积核，然后用此卷积核完成图像卷积得到输出结果就是图像高斯模糊之后的输出。
#
#  OpenCV高斯模糊 API函数
#  void GaussianBlur(
#  InputArray src,
#  OutputArray dst,
#  Size ksize, // Ksize为高斯滤波器窗口大小
#  double sigmaX, // X方向滤波系数
#  double sigmaY=0, // Y方向滤波系数
#  int borderType=BORDER_DEFAULT // 默认边缘插值方法
#  )
#  当Size(0, 0)就会从sigmax开始计算生成高斯卷积核系数，当时size不为零是优先从size开始计算高斯卷积核系数#
#

src = cv.imread("lena.bmp")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

dst1 = cv.blur(src, (5, 5))
dst2 = cv.GaussianBlur(src, (5, 5), sigmaX=15)
dst3 = cv.GaussianBlur(src, (0, 0), sigmaX=15)

cv.imshow("blur ksize=5", dst1)
cv.imshow("gaussian ksize=5", dst2)
cv.imshow("gaussian sigmax=15", dst3)

cv.waitKey(0)
cv.destroyAllWindows()


