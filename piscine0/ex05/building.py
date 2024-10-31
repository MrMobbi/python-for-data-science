
import sys


def count_punctuation(string):
    """
    count the numver of ponctuation in a string.
    """
    punctuation = '''!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~'''

    count = 0
    for char in string:
        if char in punctuation:
            count += 1

    return count


def count_digit(string):
    """
    Count the number of digit in a string.
    """
    return len(list(filter(str.isdigit, string)))


def count_sapce(string):
    """
    Count the number of space in a string.
    """
    return len(list(filter(str.isspace, string)))


def count_upper(string):
    """
    Count the number of upper case in a string.
    """
    return len(list(filter(str.isupper, string)))


def count_lower(string):
    """
    Count the number of lower case in a string.
    """
    return len(list(filter(str.islower, string)))


def display_characters(string):
    """
    display the number of character asked in the subject.
    """
    print(f"\nThe text countains {len(string)} characters:\n"
          f"{count_upper(string)} upper case\n"
          f"{count_lower(string)} lower case\n"
          f"{count_punctuation(string)} punctuation case\n"
          f"{count_sapce(string)} space case\n"
          f"{count_digit(string)} digit case")


def main():
    assert len(sys.argv) <= 2, "more than one argument is provided"
    if len(sys.argv) == 2:
        display_characters(sys.argv[1])
    else:
        print("What is the text to count?")
        display_characters(sys.stdin.readline())


if __name__ == "__main__":
    main()
