
import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:

    Return the Body Mass Index based on height (meters) and weight (kg).
    The lists must be of the same size, and the values must be either
    integers or floats. The function calculates BMI using the formula:
    BMI = weight (kg) / (height (m) ^ 2).
    """

    if len(height) != len(weight):
        raise ValueError("height and weight must have the same number of element")

    if len(height) == 0:
        raise ValueError("height and weight cannot be empty")

    for item in height:
        if not isinstance(item, (int, float)) or item <= 0:
            raise ValueError("All height must be positive integers or float")

    for item in weight:
        if not isinstance(item, (int, float)) or item <= 0:
            raise ValueError("All weight must be positive integers or float")

    matrix = np.column_stack((weight, height))
    bmi: list[int | float] = [round(raw[0] / np.square(raw[1]), 2) for raw in matrix]
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """apply_limit(bmi: list(int | float), limit: int) -> list[bool]:


    Determine if each BMI value exceeds the given limit.
    Returns a list of booleans indicating whether each BMI is above the limit.
    """

    if not isinstance(limit, int) or limit <= 0:
        raise ValueError("Limit must be an positive integers")

    for item in bmi:
        if not isinstance(item, (int, float)) or item <= 0:
            raise ValueError("BMI must be an positive integers")

    statement = np.array([item > limit for item in bmi])
    return statement
