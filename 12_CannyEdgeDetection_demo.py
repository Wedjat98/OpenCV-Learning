import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 1 图像读取
img = cv.imread('img/sleep cat.jpeg', 0)
# 2 Canny边缘检测
lowThreshold = 0
max_lowThreshold = 100
canny = cv.Canny(img, lowThreshold, max_lowThreshold)
# 3 图像展示
plt.figure(figsize=(10, 8), dpi=100)
plt.subplot(121), plt.imshow(img, cmap=plt.cm.gray), plt.title('origin')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(canny, cmap=plt.cm.gray), plt.title('Canny result')
plt.xticks([]), plt.yticks([])
plt.show()