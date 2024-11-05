
import sys


MORSE_CODE = {
    " ": "/",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
}


def check_arg(string) -> bool:
    """
    Check if the string is only alphanumeric
    """
    for c in string:
        if not c.isalnum() and not c.isspace():
            return False
    return True


def main():
    assert len(sys.argv) == 2, "the arguments are bad"
    assert check_arg(sys.argv[1]), "the arguments are bad"
    string = sys.argv[1].lower()
    count = 1
    for c in string:
        if count == len(string):
            print(MORSE_CODE[c], end="")
        else:
            print(MORSE_CODE[c], end=" ")
        count += 1
    print("")


if __name__ == "__main__":
    main()
