import psutil
import time


def transfer_image(image_file_path, destination_address):
    start_time = time.time()
    with open(image_file_path, 'rb') as f:
        image_data = f.read()
    # transfer the image data to the destination address
    # you can use libraries like requests or urllib to do this

    end_time = time.time()
    elapsed_time = end_time - start_time
    network_usage = psutil.net_io_counters().bytes_sent
    # network_usage = psutil.net_io_counters().bytes_sent / elapsed_time
    print(f"Network usage: {network_usage} bytes/second")
    print(f"elapsed_time: {elapsed_time} bytes/second")


if __name__ == '__main__':
    # example usage
    transfer_image('image.jpg', 'https://example.com/upload')
