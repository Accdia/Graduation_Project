from PIL import Image
import cv2
from scipy import ndimage
import numpy
from commpy.filters import rcosfilter
import matplotlib.pyplot as plt
import scipy

if __name__ == '__main__':
    # image = cv2.imread('../image/image.jpg')
    # image_kernel = Image.open('../image/image.jpg')
    # array = numpy.array(image_kernel, dtype=numpy.uint8, copy=True)
    # h = rcosfilter(1601, 0.5, 1, 10)[1]
    # output = ndimage.convolve(array[0], h, mode='nearest')
    beta = 0.5
    T = 1.0
    fs = 10.0

    image = Image.open('../image/image.jpg')
    array = numpy.array(image, dtype=numpy.uint8, copy=True)
    # # for line in range(0, array.shape[0]):
    # #     size = array[line].size
    # #     h = rcosfilter(100, beta, T, fs)[1]
    # #     array[line] = numpy.convolve(array[line], h, mode='same') / (T * fs)
    # # image = Image.fromarray(array)
    # # image.save('../image/rc.jpg')

    size = array[0].size
    h = rcosfilter(81, beta, T, fs)[1]
    plt.plot(h)
    plt.show()
    # array_change = numpy.convolve(array[0], h, mode='same') / (T * fs)
    # plt.subplot(3, 1, 1)
    # plt.plot(h)
    # plt.subplot(3, 1, 2)
    # plt.plot(array[0])
    # plt.subplot(3, 1, 3)
    # plt.plot(array_change)
    # plt.show()
