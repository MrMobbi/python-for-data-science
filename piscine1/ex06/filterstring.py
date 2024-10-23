
from ft_filter import ft_filter
import sys


def main():
    assert len(sys.argv) == 3, "the arguments are bad"
    assert str.isdigit(sys.argv[2]), "the arguments are bad"
    list = ft_filter(sys.argv[1], int(sys.argv[2]))
    print(list)


if __name__ == "__main__":
    main()
