import numpy as np
from scipy import fftpack, ndimage
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

# Load the image
image = cv2.imread('image.jpg', cv2.IMREAD_COLOR)

# Process the image
filtered = process_image(image)

# Display the original and filtered images
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(image)
axs[0].set_title('Original')
axs[1].imshow(filtered, cmap='gray')
axs[1].set_title('Ascending cosine filtered')
plt.show()
