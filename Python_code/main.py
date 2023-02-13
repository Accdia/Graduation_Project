# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import cv2


def gaussian_filter_2d(img, kernel_size, sigma):
    """
    Apply a 2D Gaussian filter to an image
    """
    # Create a 2D Gaussian kernel
    kernel = cv2.getGaussianKernel(kernel_size, sigma)
    kernel = np.dot(kernel, kernel.T)

    # Convolve the image with the kernel
    filtered_img = cv2.filter2D(img, -1, kernel)

    return filtered_img

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    img = cv2.imread("input.jpg")
    filtered_img = gaussian_filter_2d(img, kernel_size=5, sigma=1)
    cv2.imwrite("output.jpg", filtered_img)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
