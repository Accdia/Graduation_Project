def image_color_depth(image):
    if image.mode == 'L':
        return 8
    if image.mode == 'RGB':
        return 24
    if image.mode == 'CMYK':
        return 32


def image_size(image):
    size = list(image.size)
    return size[0] * size[1]


# 获取文件大小（可直接嵌入工程使用）
# input:文件路径
# output：文件大小，单位
import os


def GetFileSize(filepath):
    size = os.path.getsize(filepath)  # 返回的是字节大小
    '''
    为了更好地显示，应该时刻保持显示一定整数形式，即单位自适应
    '''
    if size < 1024:
        return '%i' % size + 'size'
    else:
        KBX = size / 1024
        if KBX < 1024:
            return '%.2f' % float(KBX) + 'KB'
        else:
            MBX = KBX / 1024
            if MBX < 1024:
                return '%.2f' % float(MBX) + 'MB'
            else:
                return '%.2f' % float(MBX/1024) + 'GB'
