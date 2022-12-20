import itertools


def solve_expression(n: int, m: int) -> str:
    answer = []
    big_number = ''.join([str(e) for e in range(1, n + 1)])
    plus_placements = itertools.product(('', '+'), repeat=len(big_number) - 1)

    for placement in plus_placements:
        expression = ''
        for i in range(len(placement)):
            expression += big_number[i] + placement[i]
        expression += big_number[-1]
        if eval(expression) == m:
            answer.append(f'{expression}={m}')

    return ' '.join(answer) if answer else 'no solution'


def run_tests():
    assert solve_expression(3, 1234) == 'no solution'
    assert solve_expression(10, 1) == 'no solution'
    assert solve_expression(5, 15) == '1+2+3+4+5=15'
    assert solve_expression(4, 46) == '12+34=46'
    assert solve_expression(3, 123) == '123=123'
    assert solve_expression(10, 100) == ' '.join(
        [
            '12+3+45+6+7+8+9+10=100', 
            '12+3+4+56+7+8+9+1+0=100', 
            '1+23+45+6+7+8+9+1+0=100', 
            '1+2+3+4+56+7+8+9+10=100', 
            '1+2+3+4+5+67+8+9+1+0=100'
        ]
    )
    print('\ntests OK\n')


if __name__ == '__main__':
    run_tests()
