
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
    top = ((original_heigth - crop_heigth) // 2) - 90
    bottom = ((original_heigth + crop_heigth) // 2) - 90
    left = ((original_width - crop_width) // 2) + 130
    right = ((original_width + crop_width) // 2) + 130

    cropped_img = img.crop((left, top, right, bottom))
    array_cropped = np.array(cropped_img)

    height, width = cropped_img.size
    angle = 90
    pi = 3.141592653589793
    angle_rad = angle * pi / 180.0
    center_x, center_y = width / 2, height / 2

    cos = np.cos(angle_rad)
    sin = np.sin(angle_rad)

    rotated_image = np.zeros_like(array_cropped)

    for y in range(height):
        for x in range(width):
            translated_x = x - center_x
            translated_y = y - center_y

            rotated_x = int(translated_x * cos - translated_y * sin + center_x)
            rotated_y = int(translated_x * sin + translated_y * cos + center_y)

            if 0 <= rotated_x < width and 0 <= rotated_y < height:
                rotated_image[rotated_y, rotated_x] = array_cropped[y, x]

    image_to_zoom = rotated_image
    print(f"New shape after slicing : {image_to_zoom.shape}")
    print(image_to_zoom[3])
    plt.imshow(image_to_zoom)
    plt.show()


if __name__ == "__main__":
    main()
