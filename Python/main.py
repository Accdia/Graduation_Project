# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import numpy as np
import matplotlib.pyplot as plt
import cv2
from scipy import ndimage
import os

if __name__ == '__main__':
    img = cv2.imread('image.jpg')

    # Convert the image to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply a 2D Gaussian filter with a kernel size of 5
    filtered_img = ndimage.gaussian_filter(img_gray, sigma=5)
    cv2.imwrite('filtered_image.jpg', filtered_img)

    filesize_orig = os.path.getsize('image.jpg')
    filesize_filtered = os.path.getsize('filtered_image.jpg')
    reduction_percent = (filesize_orig - filesize_filtered) / filesize_orig * 100
    print('Original Image Size: {} bytes'.format(filesize_orig))
    print('Filtered Image Size: {} bytes'.format(filesize_filtered))
    print('Reduction: {:.2f}%'.format(reduction_percent))

    # Display the original and filtered images
    # fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    # axs[0].imshow(img_gray, cmap='gray')
    # axs[0].set_title('Original Image')
    # axs[1].imshow(filtered_img, cmap='gray')
    # axs[1].set_title('Filtered Image')
    # plt.show()