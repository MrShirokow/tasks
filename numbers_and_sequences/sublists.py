'''
                                    Подсписки списка 🌶️🌶️
Подсписок — часть другого списка. Подсписок может содержать один элемент, несколько, и даже ни одного. 
Например, [1], [2], [3] и [4] — подсписки списка [1, 2, 3, 4]. Список [2, 3] — подсписок списка [1, 2, 3, 4], 
но список [2, 4] не подсписок списка [1, 2, 3, 4], так как элементы 22 и 44 во втором списке не смежные. 
Пустой список — подсписок любого списка. Сам список — подсписок самого себя, то есть список [1, 2, 3, 4] подсписок списка [1, 2, 3, 4].

На вход программе подается строка текста, содержащая символы. Из данной строки формируется список. 
Напишите программу, которая выводит список, содержащий все возможные подсписки списка, включая пустой список.

Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела.

Формат выходных данных
Программа должна вывести указанный список, содержащий все возможные подсписки, включая пустой список в соответствии с примерами.
'''

data = input().split()
length = len(data)
result = [[]]
for i in range(length):
    for j in range(length - 1):
        result.append(data[j: i + j + 1])

print(result)


'''
 sublists:|   [0]   |   [1]   |   [2]   |   [3]   | [0, 1]  |  [1, 2] |  [2, 3] | [0, 1, 2] | [1, 2, 3] | [0, 1, 2, 3] |
------------------------------------------------------------------------------------------------------------------------
    slice:| 0:0 + 1 | 1:1 + 1 | 2:2 + 1 | 3:3 + 1 | 0:0 + 2 | 1:1 + 2 | 2:2 + 2 |  0:0 + 3  |  1:1 + 3  |   0:0 + 4    |
------------------------------------------------------------------------------------------------------------------------                                                                                     
      j:  |    0    |    1    |    2    |    3    |    0    |    1    |    2    |     0     |     1     |       0      |
------------------------------------------------------------------------------------------------------------------------
      i:  |                   0                   |              1              |           2           |       3      |
------------------------------------------------------------------------------------------------------------------------
Итоговая формула для слайса: [j : j + i + 1]
'''