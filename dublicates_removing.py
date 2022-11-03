"""
Дано: список dict-объектов вида вида {"key": "value"}, например 
[{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}].

Напишите функцию, которая удаляет дубликаты из этого списка. 
Для примера выше возвращаемое значение может быть равно 
[{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {"key2": "value2"}].

Обязательное условие: функция не должна иметь сложность O(n^2).
"""

def remove_duplicates(dictionaries: list[dict]) -> list[dict]:
    checked = set()
    result = []
    for d in dictionaries:
        t = tuple(d.items())
        if t in checked:
            continue
        checked.add(t)
        result.append(d)
    return result


assert remove_duplicates([
    {"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, 
    {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}
    ]
) == [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {"key2": "value2"}]     # with and without duplicates
assert remove_duplicates([{"key1": "value1"}, {"key1": "value1"}]) == [{"key1": "value1"}]  # with duplicates
assert remove_duplicates([{"key1": "value1"}, {}]) == [{"key1": "value1"}, {}]              # without duplicates

print('Done!')
