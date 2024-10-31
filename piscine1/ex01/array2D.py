
import numpy as np


def slice_me(familly: list, start: int, end: int) -> list:
    """ """

    if not isinstance(familly, list):
        raise ValueError("Familly must be a list")

    if start >= len(familly) or end >= len(familly) or len(familly) + end < 0:
        raise ValueError("Start and End must be in the range of familly")

    print(f"")
