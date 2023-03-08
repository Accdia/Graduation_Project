import cv2
import matplotlib.pyplot as plt
from PIL import Image
import os
import Image_information

if __name__ == '__main__':
    # 读取图像
    img = cv2.imread('../image/image.jpg')

    # 高斯滤波
    blur = cv2.GaussianBlur(img, (5, 5), 0, borderType=cv2.BORDER_REPLICATE)
    cv2.imwrite('../image/blur.jpg', blur)
    blur1 = Image.open('../image/blur.jpg')
    blur2 = blur1.convert('L')
    blur2.save('../image/GaussianBlur.jpg')
    print('Original image size: ', Image_information.GetFileSize('../image/image.jpg'))
    print('GaussianBlur image size: ', Image_information.GetFileSize('../image/GaussianBlur.jpg'))
    # print('Original image size: ', os.path.getsize('../image/image.jpg'))
    # print('GaussianBlur image size: ', os.path.getsize('../image/GaussianBlur.jpg'))

    # 显示结果
    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(blur), plt.title('GaussianBlur')
    plt.xticks([]), plt.yticks([])
    plt.show()
