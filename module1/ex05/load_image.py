
from PIL import Image, ImageFile
import numpy as np


def ft_load(path: str) -> np.array:
    """ft_load(path: str) -> array:

    Load an image JPEG and JPG format and print it's  format,
    and its pixels contend in RGB format."""

    if not isinstance(path, str):
        raise ValueError("Path Must be a string format")

    try:
        with Image.open(path) as img:
            image_array = np.array(img)
        print(f"The shape of the image is: {image_array.shape}")
        return image_array

    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to open the image {path}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
