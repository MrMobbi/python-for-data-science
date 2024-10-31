
import numpy as np


def slice_me(familly: list, start: int, end: int) -> list:
    """def slice_me(familly: list, start: int, end: int) -> list:

    Prints the shape of the 2D array and returns a truncated version of the array
    based on the specified row indices. The slicing method is used to obtain the
    sub-array from start_row to end_row."""

    if not isinstance(familly, list):
        raise ValueError("Familly must be a list")

    if start >= len(familly) or end >= len(familly) or len(familly) + end < 0:
        raise ValueError("Start and End must be in the range of familly")

    print(f"")
