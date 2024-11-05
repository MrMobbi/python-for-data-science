
import numpy as np


def slice_me(familly: list, start: int, end: int) -> list:
    """def slice_me(familly: list, start: int, end: int) -> list:

    Prints the shape of the 2D array and returns a truncated version of the array
    based on the specified row indices. The slicing method is used to obtain the
    sub-array from start_row to end_row."""

    # --- Test for the list ---
    if not familly:
        raise ValueError("List cannot be empty")

    if not isinstance(familly, list):
        raise ValueError("Familly must be a list")

    first_size = len(familly[0])
    for item in familly:
        if not isinstance(item, list):
            raise ValueError("Item in the list is not a list")
        if first_size != len(item):
            raise ValueError("List are not the same size")

    # --- Test for the end and start ---
    if start < 0:
        start = len(familly) + start
    if end < 0:
        end = len(familly) + end

#   print(f"start {start} |  end {end}")

    if start >= len(familly) or end >= len(familly):
        raise ValueError("Start and End must be in the range of familly")

    if start > end:
        raise ValueError("Start cannot be greater than end")

    if start < 0 or end < 0:
        raise ValueError("Start or end cannot be bellow 0")

    if start == end:
        raise ValueError("Start and end cannot be the same")

    print(f"My shape is : ({len(familly)}, {len(familly[0])})")
    inital_array = np.array(familly)
    new_array = inital_array[start:end]
    new_list = new_array.tolist()
    print(f"My new shape is : ({len(new_list)}, {len(new_list[0])})")
    return new_list
