
import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image


def main():
    image_to_zoom = ft_load("../animal.jpeg")
    print(image_to_zoom[3])
    img = Image.fromarray(image_to_zoom)

    original_width, original_heigth = img.size
    crop_width, crop_heigth = (400, 400)

#   caluculate the new corner of the image
    top = (original_heigth - crop_heigth) // 2
    bottom = (original_heigth + crop_heigth) // 2
    left = (original_width - crop_width) // 2
    right = (original_width + crop_width) // 2

    cropped_img = img.crop((left, top, right, bottom))
    image_to_zoom = np.array(cropped_img)
    print(f"New shape after slicing : {image_to_zoom.shape}")
    print(image_to_zoom[3])
    plt.imshow(image_to_zoom)
    plt.show()


if __name__ == "__main__":
    main()
