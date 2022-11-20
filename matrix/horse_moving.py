"""
                        Ходы коня
На шахматной доске 8 x 8 стоит конь. Напишите программу, которая отмечает положение коня на доске и все клетки, которые бьет конь. 
Клетку, где стоит конь, отметьте английской буквой N, клетки, которые бьет конь, отметьте символами *, остальные клетки заполните точками.

Формат входных данных
На вход программе подаются координаты коня на шахматной доске в шахматной нотации (то есть в виде e4, где сначала записывается номер столбца 
(буква от a до h, слева направо), затем номеру строки (цифра от 1 до 8, снизу вверх)).

Формат выходных данных
Программа должна вывести на экран изображение доски, разделяя элементы пробелами.
"""

position = input()
x, y = ord(position[0]) - 97, 8 - int(position[1])

board = [['.*'[abs((x - j) * (y - i)) == 2] for j in range(8)] for i in range(8)]
board[y][x] = 'N'
[print(*row) for row in board]