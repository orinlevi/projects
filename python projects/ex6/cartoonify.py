##############################################################################
# FILE: cartoonify.py
# WRITERS: orin levi , orin.levi , 206440075
# EXERCISE: Intro2cs2 ex6 2021-2022
# DESCRIPTION: program that create a cartoon picture.
##############################################################################

##############################################################################
#                                   Imports                                  #
##############################################################################
from ex6_helper import *
from typing import Optional
import copy
import math
import sys


def matrices_creator(rows, columns=0):
    """
    create an empty matrix according to the number of rows and columns desired
    :param rows: the num of desired rows
    :param columns: the num of desired columns
    :return: an "empty" matrix
    """
    matrices = []
    for row in range(rows):
        matrices.append([])
        for column in range(columns):
            matrices[row].append([])
    return matrices


def separate_channels(image: ColoredImage) -> List[List[List[int]]]:
    """
    separate a colorful picture to multiple pics in one color channel
    :param image: an image/photo  (represent by 3D matrices)
    (if the pic are black ant white it's already "separate" and represented
    by 2D matrix)
    :return: a list of multiple pics in one color
    channel (represented by 2D matrices)
    """
    channel_matrices = matrices_creator(len(image[0][0]), len(image))
    for row in range(len(image)):
        for column in range(len(image[row])):
            for channel in range(len(image[row][column])):
                channel_matrices[channel][row].append(
                    image[row][column][channel])
    return channel_matrices


def combine_channels(channels: List[List[List[int]]]) -> ColoredImage:
    """
    reverses the previous function and combine between between the channels
    :param channels: a list of multiple pics in one color
    channel (represented by 2D matrices)
    :return: an image/photo  (represent by 3D matrices)
    (if the pic are black ant white it's already "separate" and represented
    by 2D matrix)
    """
    pic = matrices_creator(len(channels[0]), len(channels[0][0]))
    for channel in range(len(channels)):
        for row in range(len(channels[channel])):
            for column in range(len(channels[channel][row])):
                pic[row][column].append(channels[channel][row][column])
    return pic


def RGB2grayscale(colored_image: ColoredImage) -> SingleChannelImage:
    """
    make a colorful pic to a black and whith pic
    :param colored_image: colorful pic (represent by 3D matrices)
    (if the pic are black ant white it's already "separate" and represented
    by 2D matrix)
    :return: black and white pic (represented by 2D matrices)
    """
    black_white_image = matrices_creator(len(colored_image))
    for row in range(len(colored_image)):
        for column in range(len(colored_image[row])):
            pixel_color = colored_image[row][column]
            black_white_pixel = round(pixel_color[0] * 0.299 + pixel_color[
                1] * 0.587 + pixel_color[2] * 0.114)
            black_white_image[row].append(black_white_pixel)
    return black_white_image


def blur_kernel(size: int) -> Kernel:
    """

    :param size:
    :return:
    """
    kernel = []
    for row in range(size):
        kernel.append([])
        for column in range(size):
            kernel[row].append(1 / size ** 2)
    return kernel


def kernel_helper(row, column, kernel, image):
    """

    :param row:
    :param column:
    :param kernel:
    :param image:
    :return:
    """
    r = len(kernel) // 2
    row_kernel = 0
    column_kernel = 0
    blur_pixel_color = 0
    for row_i in range(row - r, row + r + 1):
        for column_i in range(column - r, column + r + 1):
            if 0 <= row_i < len(image) and 0 <= column_i < len(image[0]):
                blur_pixel_color += kernel[row_kernel][column_kernel] * \
                                    image[row_i][column_i]
                column_kernel += 1
            else:
                blur_pixel_color += kernel[row_kernel][column_kernel] * \
                                    image[row][column]
                column_kernel += 1
        column_kernel = 0
        row_kernel += 1
    return blur_pixel_color


def apply_kernel(image: SingleChannelImage, kernel: Kernel) -> SingleChannelImage:
    """

    :param image:
    :param kernel:
    :return:
    """
    blur_image = copy.deepcopy(image)
    for row in range(len(image)):
        for column in range(len(image[row])):
            blur_pixel_color = kernel_helper(row, column, kernel, image)
            if blur_pixel_color < 0:
                blur_pixel_color = 0
            elif blur_pixel_color > 255:
                blur_pixel_color = 255
            blur_pixel_color = int(blur_pixel_color + 0.5)
            blur_image[row][column] = blur_pixel_color
    return blur_image


def bilinear_interpolation(image: SingleChannelImage, y: float, x: float) -> int:
    """

    :param image:
    :param y:
    :param x:
    :return:
    """
    y_floor = math.floor(y)
    x_floor = math.floor(x)
    if y == int(y):
        y_floor -= 1
    if x == int(x):
        x_floor -= 1
    a = image[y_floor][x_floor]
    b = image[math.ceil(y)][x_floor]
    c = image[y_floor][math.ceil(x)]
    d = image[math.ceil(y)][math.ceil(x)]
    d_x = x - x_floor
    d_y = y - y_floor
    pixel_color = int(((a * (1 - d_x) * (1 - d_y)) + b * d_y
                        * (1 - d_x) + c * d_x * (1 - d_y) + d *
                        d_x * d_y) + 0.5)
    return pixel_color


def resize(image: SingleChannelImage, new_height: int, new_width: int) -> SingleChannelImage:
    """

    :param image:
    :param new_height:
    :param new_width:
    :return:
    """
    old_height = len(image) - 1
    old_width = len(image[0]) - 1
    height_ratio = old_height / (new_height - 1)
    width_ratio = old_width / (new_width - 1)
    new_image = matrices_creator(new_height, new_width)
    for row in range(new_height):
        for column in range(new_width):
            y = row * height_ratio
            x = column * width_ratio
            new_image[row][column] = bilinear_interpolation(image, y, x)
    return new_image


def scale_down_colored_image(image: ColoredImage, max_size: int) -> Optional[ColoredImage]:
    """

    :param image:
    :param max_size:
    :return:
    """
    high = len(image)
    width = len(image[0])
    new_high = 0
    new_width = 0
    if (high <= max_size) and (width <= max_size):
        return None
    else:
        max_width_height = max(high, width)
        if max_width_height == width:
            new_width = max_size
            new_high = int(((max_size * high) / width) + 0.5)
        elif max_width_height == high:
            new_high = max_size
            new_width = int(((max_size * width) / high) + 0.5)
        channels = separate_channels(image)
        resized_channels = []
        for channel in channels:
            resized_channel = resize(channel, new_high, new_width)
            resized_channels.append(resized_channel)
        new_image = combine_channels(resized_channels)
        return new_image


def rotate_90(image: Image, direction: str) -> Image:
    """

    :param image:
    :param direction:
    :return:
    """
    inverted_image = matrices_creator(len(image[0]))
    if direction == 'R':
        for row_r in range(len(image) - 1, -1, -1):
            for column_r in range(len(image[0])):
                inverted_image[column_r].append(image[row_r][column_r])
    elif direction == 'L':
        for row_l in range(len(image)):
            for column_l in range(len(image[0]) - 1, -1, -1):
                inverted_image[column_l].append(image[row_l][column_l])
    if direction == 'L':
        mirror_image_of_image = []
        for row in range(len(inverted_image) - 1, -1, -1):
            mirror_image_of_image.append(inverted_image[row])
        inverted_image = mirror_image_of_image
    return inverted_image


def _kernel_1(size):
    """

    :param size:
    :return:
    """
    kernel = matrices_creator(size, size)
    for i in range(size):
        for j in range(size):
            kernel[i][j] = 1
    return kernel


def get_edges(image: SingleChannelImage, blur_size: int, block_size: int, c: int) -> SingleChannelImage:
    """

    :param image:
    :param blur_size:
    :param block_size:
    :param c:
    :return:
    """
    edges_image = matrices_creator(len(image))
    blur_image = apply_kernel(image, blur_kernel(blur_size))
    black_or_white = 0
    kernel_1 = _kernel_1(block_size)
    for row in range(len(blur_image)):
        for column in range(len(blur_image[row])):
            old_pixel_color = blur_image[row][column]
            threshold = ((kernel_helper(row, column, kernel_1, blur_image))/(
                block_size ** 2)) - c
            if old_pixel_color < threshold:
                black_or_white = 0
            elif old_pixel_color > threshold:
                black_or_white = 255
            edges_image[row].append(black_or_white)
    return edges_image


def quantize(image: SingleChannelImage, N: int) -> SingleChannelImage:
    """

    :param image:
    :param N:
    :return:
    """
    quantize_image = copy.deepcopy(image)
    for row in range(len(image)):
        for column in range(len(image[0])):
            quantize_image[row][column] = round(math.floor(image[row][
                column] * (N / 256)) * (255 / (N - 1)))
    return quantize_image


def quantize_colored_image(image: ColoredImage, N: int) -> ColoredImage:
    """

    :param image:
    :param N:
    :return:
    """
    channels = separate_channels(image)
    matrix_before_combine = copy.deepcopy(channels)
    for matrices in range(len(channels)):
        matrix_before_combine[matrices] = quantize(channels[matrices], N)
    quantize_image = combine_channels(matrix_before_combine)
    return quantize_image


def add_mask(image1: Image, image2: Image, mask: List[List[float]]) -> Image:
    """

    :param image1:
    :param image2:
    :param mask:
    :return:
    """
    new_image = []
    if type(image1[0][0]) is not list:
        mask_image = matrices_creator(len(mask))
        for i in range(len(mask)):
            for j in range(len(mask[0])):
                mask_image[i].append(int(round(image1[i][j] * mask[i][j]) + (
                    image2[i][j] * (1 - mask[i][j]))))
        new_image = mask_image
    else:
        channels_image1 = separate_channels(image1)
        channels_image2 = separate_channels(image2)
        mask_channels_image = matrices_creator(len(channels_image1),
            len(channels_image1[0]))
        for channel in range(len(mask_channels_image)):
            for row in range(len(image1)):
                for column in range(len(image1[0])):
                    mask_channels_image[channel][row].append(int(round(
                        (channels_image1[channel][row][column] * mask[row][
                            column]) + (channels_image2[channel][row][column]
                                        * (1 - mask[row][column])))))
        new_image = combine_channels(mask_channels_image)
    return new_image


def mask_creator(black_white_image):
    """

    :param black_white_image:
    :return:
    """
    mask = copy.deepcopy(black_white_image)
    for row in range(len(black_white_image)):
        for column in range(len(black_white_image[0])):
            mask[row][column] = black_white_image[row][column] / 255
    return mask


def duplicate_channels(image, num_of_channels):
    duplicate_matrix = []
    for channel in range(num_of_channels):
        duplicate_matrix.append(copy.deepcopy(image))
    new_matrix = combine_channels(duplicate_matrix)
    return new_matrix


def cartoonify(image: ColoredImage, blur_size: int, th_block_size: int,
               th_c: int, quant_num_shades: int) -> ColoredImage:
    """

    :param image:
    :param blur_size:
    :param th_block_size:
    :param th_c:
    :param quant_num_shades:
    :return:
    """
    new_color_image = quantize_colored_image(image, quant_num_shades)
    black_white_image = RGB2grayscale(image)
    edges_image = get_edges(black_white_image, blur_size, th_block_size, th_c)
    edges_image_3d = duplicate_channels(edges_image, len(image[0][0]))
    mask = mask_creator(edges_image)
    new_image = add_mask(new_color_image, edges_image_3d, mask)
    return new_image


if __name__ == '__main__':
    arg = sys.argv
    try:
        if len(arg) != 8:
            raise ValueError
    except ValueError as v:
        exit()
    image = load_image(arg[1])
    checks_image_size_deviation = scale_down_colored_image(image, int(arg[
        3]))
    thumbnail = checks_image_size_deviation
    if checks_image_size_deviation is None:
        cartoon_pic = cartoonify(image, int(arg[4]), int(arg[5]), int(arg[6]),
            int(arg[7]))
        save_image(cartoon_pic, sys.argv[2])
    else:
        cartoon_thumbnail = cartoonify(thumbnail, int(arg[4]), int(arg[5]),
            int(arg[6]), int(arg[7]))
        save_image(cartoon_thumbnail, sys.argv[2])

