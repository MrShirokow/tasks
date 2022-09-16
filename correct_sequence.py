def check_sequence(sequence: str) -> bool:
    validator = 0
    operations = {"(": 1, ")": -1}
    for bracket in sequence:
        validator += operations[bracket]
        if validator < 0:
            return False
    return True if validator == 0 else False


def main():
    sequence = input()
    print(check_sequence(sequence))


if __name__ == '__main__':
    main()
