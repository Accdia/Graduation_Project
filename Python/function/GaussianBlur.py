import cv2
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # 读取图像
    img = cv2.imread('../image/image.jpg')

    # 高斯滤波
    blur = cv2.GaussianBlur(img,(5,5),0,borderType=cv2.BORDER_REPLICATE)
    # cv2.imwrite('blur.jpg', blur)

    # 显示结果
    plt.subplot(121),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(blur),plt.title('GaussianBlur')
    plt.xticks([]), plt.yticks([])
    plt.show()
