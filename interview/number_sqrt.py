def check_positive(number: int):
    if number < 0:
        raise ValueError('number should be positive')


def get_sqrt_by_degree(number: int) -> int | None:
    """ 
    За рамки условия вроде не выходит, но ниже опишу алгоритм, который первый пришёл в голову
    """
    check_positive(number)
    checked_value = number ** 0.5
    return int(checked_value) if checked_value == int(checked_value) else None


def get_sqrt(number: int) -> int | None:
    check_positive(number)
    sqrt = 0
    while sqrt * sqrt < number:
        sqrt += 1
    if sqrt * sqrt > number:
        return None
    return sqrt


def main():
    number = int(input())
    # print(get_sqrt_by_degree(number))
    print(get_sqrt(number))


if __name__ == '__main__':
    main()
