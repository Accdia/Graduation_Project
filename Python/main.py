# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    img = plt.imread('image.jpg')

    # Convert the image to grayscale
    img_gray = np.mean(img, axis=2)

    # Apply a 2D Gaussian filter with a kernel size of 5
    filtered_img = ndimage.gaussian_filter(img_gray, sigma=5)

    # Display the original and filtered images
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(img_gray, cmap='gray')
    axs[0].set_title('Original Image')
    axs[1].imshow(filtered_img, cmap='gray')
    axs[1].set_title('Filtered Image')
    plt.show()