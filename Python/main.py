import os
import sys
from PIL import Image

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from function import Image_information

if __name__ == '__main__':
    image_colr_depth = Image_information.image_color_depth(Image.open('image/image.jpg'))
    image_size = Image_information.image_size(Image.open('image/image.jpg'))
    print(image_colr_depth, image_size)
