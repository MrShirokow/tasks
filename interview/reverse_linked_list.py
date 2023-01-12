
from __future__ import annotations
from typing import Optional
from dataclasses import dataclass


@dataclass
class Node:
    value: int
    next: Optional[Node]
    

class LinkedList:
    def __init__(self, head: Optional[Node]) -> None:
        self.head = head
    
    def reverse(self):
        previous_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node


if __name__ == '__main__':
    linked_list = LinkedList(
        head=Node(
            value=1,
            next=Node(
                value=2,
                next=Node(
                    value=3,
                    next=Node(
                        value=4,
                        next=None
                    )
                )
            )
        )
    )
    linked_list.reverse()
    assert linked_list.head.value == 4
    assert linked_list.head.next.value == 3
    assert linked_list.head.next.next.value == 2
    assert linked_list.head.next.next.next.value == 1
    assert linked_list.head.next.next.next.next is None
    print('\nTests OK\n')
