'''
                                    Орел и решка
Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки. 
Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.

Формат входных данных
На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".

Формат выходных данных
Программа должна вывести наибольшее количество подряд выпавших Решек.

Примечание. Если выпавших Решек нет, то необходимо вывести число 0.
'''


import re

string = input()
pattern = re.compile(r'Р+')
result = re.findall(pattern, string)
result.sort(key=len)
print(0 if len(result) == 0 else len(result[-1]))

# Лаконичное решение
print(len(max(string.split('О'))))