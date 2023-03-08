import numpy as np
import psutil
import time
import matplotlib.pyplot as plt
import cv2
from scipy.ndimage import gaussian_filter


def ascending_cosine_filter(size):
    """
    Generate an ascending cosine filter of the given size.
    """
    x = np.arange(size) - size // 2
    y = np.arange(size) - size // 2
    xx, yy = np.meshgrid(x, y)
    dist = np.sqrt(xx ** 2 + yy ** 2)
    angle = np.arctan2(yy, xx)
    angle[angle < 0] += 2 * np.pi
    return np.cos(angle) * (dist < size // 2)


def process_image(image):
    """
    Process the given image using a Gaussian filter.
    """
    # Convert the image to grayscale if necessary
    if len(image.shape) == 3:
        image = np.mean(image, axis=2)

    # Apply the Gaussian filter
    filtered = gaussian_filter(image, sigma=2)

    # Normalize the filtered image
    filtered = (filtered - np.min(filtered)) / (np.max(filtered) - np.min(filtered))

    return filtered


def transfer_image(image_file_path, destination_address, filter_name):
    start_time = time.time()
    with open(image_file_path, 'rb') as f:
        image_data = f.read()
    # transfer the image data to the destination address
    # you can use libraries like requests or urllib to do this

    end_time = time.time()
    elapsed_time = end_time - start_time
    network_usage = psutil.net_io_counters().bytes_sent
    # network_usage = psutil.net_io_counters().bytes_sent / elapsed_time
    print(f"{filter_name} Network usage: {network_usage} bytes/second")
    # print(f"elapsed_time: {elapsed_time} bytes/second")


if __name__ == '__main__':
    # Load the image
    image = cv2.imread('../image/image.jpg', cv2.IMREAD_COLOR)
    transfer_image('../image/image.jpg', 'https://example.com/upload', 'original')

    kernel = np.ones((5, 5), np.float32) / 25
    smoothed = cv2.filter2D(image, -1, kernel)
    cv2.imwrite('../image/smoothed.jpg', smoothed)
    transfer_image('../image/smoothed.jpg', 'https://example.com/upload', 'smoothed')

    # Process the image
    blur = process_image(image)
    cv2.imwrite('../image/blur.jpg', blur)
    transfer_image('../image/blur.jpg', 'https://example.com/upload', 'blur')

    median = cv2.medianBlur(image, 5)
    cv2.imwrite('../image/median.jpg', median)
    transfer_image('../image/median.jpg', 'https://example.com/upload', 'median')

    # Display the original and filtered images
    fig, axs = plt.subplots(1, 4, figsize=(10, 5))
    axs[0].imshow(image)
    axs[0].set_title('Original')
    axs[1].imshow(blur, cmap='gray')
    axs[1].set_title('blur')
    axs[2].imshow(median, cmap='gray')
    axs[2].set_title('median')
    axs[3].imshow(smoothed, cmap='gray')
    axs[3].set_title('smoothed')
    plt.show()