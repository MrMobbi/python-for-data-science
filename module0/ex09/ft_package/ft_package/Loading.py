
import os


def ft_tqdm(lst: range) -> None:
    """
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.
    """
    total = len(lst)
    try:
        length_bar = os.get_terminal_size().columns - 37  # built-in function
    except OSError:
        length_bar = 60
    fill = '█'

    def print_progressbar(iteration):
        """
        logic for printing the progressbar
        """
        percent = int(100 * (iteration / int(total)))
        bar_fill = int(length_bar * iteration // total)
        bar = fill * bar_fill + ' ' * (length_bar - bar_fill)
        print(f"{percent}%|{bar}| {iteration}/{total}", end='\r')

    print_progressbar(0)
    for i, elem in enumerate(lst):
        yield elem
        print_progressbar(i + 1)

    print()
