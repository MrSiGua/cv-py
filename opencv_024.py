import cv2 as cv
import numpy as np

# 图像噪声
#
# 图像噪声产生的原因很复杂，有的可能是数字信号在传输过程中发生了丢失或者受到干扰，有的是成像设备或者环境本身导致成像质量不稳定，反应到图像上就是图像的亮度与颜色呈现某种程度的不一致性。从噪声的类型上，常见的图像噪声可以分为如下几种：
#
# - 椒盐噪声，
# 是一种随机在图像中出现的稀疏分布的黑白像素点， 对椒盐噪声一种有效的去噪手段就是图像中值滤波
#
# - 高斯噪声/符合高斯分布
# 一般会在数码相机的图像采集(acquisition)阶段发生,这个时候它的物理/电/光等各种信号都可能导致产生高斯分布噪声。
#
# - 均匀分布噪声
# 均匀/规则噪声一般都是因为某些规律性的错误导致的
#
# 代码演示
# - 图像椒盐噪声生成
# - 图像高斯噪声生成#


def add_salt_pepper_noise(image):
    h, w = image.shape[:2]
    nums = 10000
    rows = np.random.randint(0, h, nums, dtype=np.int)
    cols = np.random.randint(0, w, nums, dtype=np.int)
    for i in range(nums):
        if i % 2 == 1:
            image[rows[i], cols[i]] = (255, 255, 255)
        else:
            image[rows[i], cols[i]] = (0, 0, 0)
    return image


def gaussian_noise(image):
    noise = np.zeros(image.shape, image.dtype)
    m = (15, 15, 15)
    s = (30, 30, 30)
    cv.randn(noise, m, s)
    dst = cv.add(image, noise)
    cv.imshow("gaussian noise", dst)
    return dst


src = cv.imread("cos.jpg")
h, w = src.shape[:2]
copy = np.copy(src)
copy = add_salt_pepper_noise(copy)

result = np.zeros([h, w*2, 3], dtype=src.dtype)
result[0:h,0:w,:] = src
result[0:h,w:2*w,:] = copy
cv.putText(result, "original image", (10, 30), cv.FONT_HERSHEY_PLAIN, 2.0, (0, 255, 255), 1)
cv.putText(result, "salt pepper image", (w+10, 30), cv.FONT_HERSHEY_PLAIN, 2.0, (0, 255, 255), 1)
cv.imshow("salt pepper noise", result)
cv.imwrite("D:/result.png", result)

cv.waitKey(0)
cv.destroyAllWindows()


