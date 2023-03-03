import psutil
import time
import cv2
import matplotlib.pyplot as plt


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
    img = cv2.imread('image/image.jpg', cv2.IMREAD_COLOR)
    transfer_image('image/image.jpg', 'https://example.com/upload', 'original')

    blur = cv2.GaussianBlur(img, (5, 5), 0)
    cv2.imwrite('image/blur.jpg', blur)
    transfer_image('image/blur.jpg', 'https://example.com/upload', 'blur')

    median = cv2.medianBlur(img, 5)
    cv2.imwrite('image/median.jpg', median)
    transfer_image('image/median.jpg', 'https://example.com/upload', 'median')







