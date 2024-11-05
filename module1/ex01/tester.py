
from array2D import slice_me


def main():
    test = [
        [1.80, 'coucou'],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2],
    ]
    print(slice_me(test, 0, 2))
    print(slice_me(test, 1, -2))


if __name__ == "__main__":
    main()
