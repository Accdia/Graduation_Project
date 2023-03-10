import cv2

# # 动态的将搜索路径添加到sys.path中
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from function import GaussianBlur, Image_information

if __name__ == '__main__':
    image = cv2.imread('image/image.jpg')
    print('Original image size= ', Image_information.GetFileSize('image/image.jpg'))
    for size in range(3, 17, 2):
        GaussianBlur.gaussian(size, image)
    # image = GaussianBlur.gaussian(5, cv2.imread('image/image.jpg'))

    # print('Original image size: ', Image_information.GetFileSize('image/image.jpg'))
    # print('GaussianBlur image size: ', Image_information.GetFileSize('image/GaussianBlur.jpg'))  # 获取文件大小

    # image_colr_depth = Image_information.image_color_depth(Image.open('image/image.jpg'))
    # image_size = Image_information.image_size(Image.open('image/image.jpg'))
    # print(image_colr_depth, image_size)
