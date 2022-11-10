from collections import Counter, defaultdict


def find_most_common_with_cheats(string: str) -> tuple:
    return Counter(string.lower()).most_common(1)[0]


def find_most_common_without_cheats(string: str) -> tuple:
    """
    Сначала пришла эта идея, со словарём, но следом вспомнил про Counter
    """
    counter = defaultdict(int)
    for char in string.lower():
        counter[char] += 1
    result = sorted(counter.items(), key=lambda pair: pair[1])[-1]
    return result


def main():
    input_str = input()
    # print(find_most_common_with_cheats(input_str))
    print(find_most_common_without_cheats(input_str))

    
if __name__ == '__main__':
    main()
