import cv2
import numpy as np
from matplotlib import pyplot as plt


def low_pass_filter(img, sigma):
    rows, cols = img.shape
    crow, ccol = rows // 2, cols // 2
    x = np.linspace(0, cols - 1, cols)
    y = np.linspace(0, rows - 1, rows)
    xv, yv = np.meshgrid(x, y)
    d = np.sqrt((xv - ccol) ** 2 + (yv - crow) ** 2)
    kernel = cv2.getGaussianKernel(rows, sigma) * cv2.getGaussianKernel(cols, sigma).T
    kernel = kernel / np.max(kernel)
    fft_img = np.fft.fft2(img)
    fft_shifted = np.fft.fftshift(fft_img)
    filtered = fft_shifted * kernel
    filtered_shifted = np.fft.ifftshift(filtered)
    filtered_img = np.fft.ifft2(filtered_shifted)
    filtered_img = np.abs(filtered_img)
    return filtered_img


if __name__ == '__main__':
    # Load the image
    img = cv2.imread('image.jpg', 0)

    # Apply the 2D Fourier Transform to the image
    f = np.fft.fft2(img)

    # Shift the zero-frequency component to the center of the spectrum
    fshift = np.fft.fftshift(f)

    # Compute the magnitude spectrum (absolute value) of the Fourier Transform
    magnitude_spectrum = 20 * np.log(np.abs(fshift))

    # Display the magnitude spectrum using Matplotlib
    plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()

    # Apply the low-pass filter to the magnitude spectrum of the Fourier Transform of the image
    sigma = 20
    filtered_spectrum = low_pass_filter(magnitude_spectrum, sigma)

    # Display the filtered magnitude spectrum using Matplotlib
    plt.imshow(filtered_spectrum, cmap='gray')
    plt.title('Filtered Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()

    # Compute the filtered image by taking the inverse Fourier Transform of the filtered frequency domain representation
    filtered_fshift = np.fft.ifftshift(filtered_spectrum)
    filtered_f = np.fft.ifft2(filtered_fshift)
    filtered_img = np.abs(filtered_f)

    # Display the filtered image using Matplotlib
    plt.imshow(filtered_img, cmap='gray')
    plt.title('Filtered Image'), plt.xticks([]), plt.yticks([])
    plt.show()

    # Display the original and filtered image side by side using Matplotlib
    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(filtered_img, cmap='gray')
    plt.title('Filtered Image'), plt.xticks([]), plt.yticks([])
    plt.show()
