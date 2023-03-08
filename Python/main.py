import os
import sys

import cv2
from PIL import Image

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from function import GaussianBlur

if __name__ == '__main__':
    image = GaussianBlur.gaussian(cv2.imread('image/image.jpg'))
    # print('Original image size: ', Image_information.GetFileSize('image/image.jpg'))
    # print('GaussianBlur image size: ', Image_information.GetFileSize('image/GaussianBlur.jpg'))  # 获取文件大小

    # image_colr_depth = Image_information.image_color_depth(Image.open('image/image.jpg'))
    # image_size = Image_information.image_size(Image.open('image/image.jpg'))
    # print(image_colr_depth, image_size)
