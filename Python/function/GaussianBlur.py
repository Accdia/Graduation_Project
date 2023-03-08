import cv2
from PIL import Image
import numpy
from function import Image_information


def gaussian(size, image):
    # image = cv2.imread(path)  # 读取图像
    # 高斯滤波
    blur = cv2.GaussianBlur(image, (size, size), 0, borderType=cv2.BORDER_REPLICATE)
    # 将数组转为图像
    blur = Image.fromarray(numpy.uint8(blur))
    # 将图像位深度转为8位
    blur = blur.convert('L')
    # 保存图像
    blur.save('image' + '/GaussianBlur_' + str(size) + '.jpg')
    # blur.save('image/GaussianBlur.jpg')
    # 输出文件大小
    print('GaussianBlur size =', size, 'image size =',
          Image_information.GetFileSize('image' + '/GaussianBlur_' + str(size) + '.jpg'))
    # print('Original image size: ', Image_information.GetFileSize('image/image.jpg'))
    # print('GaussianBlur image size: ', Image_information.GetFileSize('image/GaussianBlur.jpg'))  # 获取文件大小

    return blur

# if __name__ == '__main__':
#     image = cv2.imread('../image/image.jpg')  # 读取图像
#     blur = cv2.GaussianBlur(image, (7, 7), 0, borderType=cv2.BORDER_REPLICATE)  # 高斯滤波
#     blur = Image.fromarray(numpy.uint8(blur))  # 将数组转为图像
#     blur = blur.convert('L')  # 将图像位深度转为8位
#     blur.save('../image/GaussianBlur.jpg')  # 保存图像
#     print('Original image size: ', Image_information.GetFileSize('../image/image.jpg'))
#     print('GaussianBlur image size: ', Image_information.GetFileSize('../image/GaussianBlur.jpg'))  # 获取文件大小

    # # 读取图像
    # img = cv2.imread('../image/image.jpg')
    #
    # # 高斯滤波
    # blur = cv2.GaussianBlur(img, (5, 5), 0, borderType=cv2.BORDER_REPLICATE)
    # cv2.imwrite('../image/blur.jpg', blur)
    # blur1 = Image.open('../image/blur.jpg')
    # blur2 = blur1.convert('L')
    # blur2.save('../image/GaussianBlur.jpg')
    # print('Original image size: ', Image_information.GetFileSize('../image/image.jpg'))
    # print('GaussianBlur image size: ', Image_information.GetFileSize('../image/GaussianBlur.jpg'))
