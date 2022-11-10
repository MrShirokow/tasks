"""
Есть 100 билетов на мероприятия, пронумерованные от 1 до 100. 
Один потеряли. Нужно найти номер потерянного билета.
"""


def find_lost_ticket(tickets: list) -> int:
    full_sum = 5050    # n * (A1 + An) / 2
    tickets_sum = sum(tickets)
    return full_sum - tickets_sum


assert find_lost_ticket([e for e in range(1, 100)]) == 100
assert find_lost_ticket([e for e in range(1, 101) if e != 99]) == 99
assert find_lost_ticket([e for e in range(1, 101) if e != 1]) == 1

print('Done')