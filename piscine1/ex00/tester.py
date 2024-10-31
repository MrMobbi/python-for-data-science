
from give_bmi import apply_limit, give_bmi


def main():
    height_int: list[float] = [1.75, 1.80, 2.12, 1.57, 1.40]
    weight_int: list[int] = [60, 80, 120, 50, 42]

    bmi = give_bmi(height_int, weight_int)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 20))


if __name__ == "__main__":
    main()
