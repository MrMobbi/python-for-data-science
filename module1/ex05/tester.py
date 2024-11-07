
from pimp_image import ft_blue, \
    ft_invert, \
    ft_green, \
    ft_grey, \
    ft_red
from load_image import ft_load
from PIL import Image
import matplotlib.pyplot as plt


def main():
    img_orginal = ft_load("../landscape.jpg")

    img_modified = ft_grey(img_orginal)
    img = Image.fromarray(img_modified)
    plt.imshow(img)
    plt.show()


if __name__ == "__main__":
    main()
