import cv2
import numpy

# # 动态的将搜索路径添加到sys.path中
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from function import GaussianBlur, Image_information, rrcfileters

if __name__ == '__main__':
    image = cv2.imread('image/image.jpg')
    print('Original image size= ', Image_information.getfilesize('image/image.jpg'))
    for size in range(3, 17, 2):
        GaussianBlur.gaussian(size, image)
