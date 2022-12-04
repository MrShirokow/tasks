"""
https://www.geeksforgeeks.org/find-the-pair-a-b-with-minimum-lcm-such-that-their-sum-is-equal-to-n/
"""


def is_prime(n):
    if (n == 1):
        return False
    for i in range(2, n + 1):
        if i * i > n:
            break
        if (n % i == 0):
            return False
    return True
 

def find_numbers(n):
    if is_prime(n):
        return 1, n - 1
    else:
        for i in range(2, n + 1):
            if i * i > n:
                break
            if (n % i == 0):
                return n // i, n // i * (i - 1)


def main():
    assert find_numbers(9) == (3, 6)
    assert find_numbers(4) == (2, 2)
    assert find_numbers(3) == (1, 2)
    assert find_numbers(1_000_000_000) == (500_000_000, 500_000_000)
    print('\ntests done\n')


if __name__ == '__main__':
    main()
