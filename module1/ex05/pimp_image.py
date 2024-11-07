
import numpy as np


def ft_invert(array) -> np.array:
    """Invert the pixel of an image"""
    array = 255 - array
    return array


def ft_red(array: np.array) -> np.array:
    """Turn the image red"""
    array[:, :, 1] *= 0
    array[:, :, 2] *= 0
    return array


def ft_green(array) -> np.array:
    array[:, :, 0] -= array[:, :, 0]
    array[:, :, 2] -= array[:, :, 2]
    return array


def ft_blue(array) -> np.array:
    """Turn the image blue"""
    array[:, :, 0] = 0
    array[:, :, 1] = 0
    return array


def ft_grey(array) -> np.array:
    """turn the image kind of grey"""
    array[:, :, 0] = array[:, :, 1]
    array[:, :, 2] = array[:, :, 1]
    return array
