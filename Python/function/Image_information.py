def image_color_depth(image):
    if image.mode == 'L':
        return 8
    if image.mode == 'RGB':
        return 24
    if image.mode == 'CMYK':
        return 32
    # return image.getbands


def image_size(image):
    size = list(image.size)
    return size[0] * size[1]
