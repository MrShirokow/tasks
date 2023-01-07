


def compress(raw_string: str) -> str:
    if raw_string == '':
        return raw_string
    compressed = ''
    previous = raw_string[0]
    count = 1
    for e in raw_string[1:]:
        if e == previous:
            count += 1
            continue
        compressed += previous + (str(count) if count > 1 else '')
        previous = e
        count = 1
    compressed += previous + (str(count) if count > 1 else '')
    return compressed


if __name__ == '__main__':
    assert compress('abbehhhhhtaaa') == 'ab2eh5ta3'
    assert compress('') == ''
    assert compress('a') == 'a'
    assert compress('aaa') == 'a3'
    assert compress('aaab') == 'a3b'
    assert compress('aaabb') == 'a3b2'
    assert compress('aaabaaa') == 'a3ba3'
    assert compress('abcde') == 'abcde'
