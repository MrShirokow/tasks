"""
https://leetcode.com/problems/add-two-numbers/
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = ListNode()
        current = result
        while l1 or l2 or carry:
            first = l1.val if l1 else 0
            second = l2.val if l2 else 0

            summ = first + second + carry
            val, carry = summ % 10, summ // 10

            current.next = ListNode(val)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return result.next


if __name__ == '__main__':
    solution = Solution()
    answer = solution.addTwoNumbers(
        ListNode(2, 
            ListNode(4, 
                ListNode(3)
            )
        ), 
        ListNode(5, 
            ListNode(6, 
                ListNode(4)
            )
        )
    )
    assert answer.val == 7
    assert answer.next.val == 0
    assert answer.next.next.val == 8
    assert answer.next.next.next is None
    answer = solution.addTwoNumbers(ListNode(0), ListNode(0))
    assert answer.val == 0
    assert answer.next is None
    answer = solution.addTwoNumbers(
        ListNode(9, 
            ListNode(9, 
                ListNode(9, 
                    ListNode(9, 
                        ListNode(9, 
                            ListNode(9, 
                                ListNode(9)
                            )
                        )
                    )
                )
            )
        ),
        ListNode(9,
            ListNode(9,
                ListNode(9,
                    ListNode(9)
                )
            )
        )
    )
    assert answer.val == 8
    assert answer.next.val == 9
    assert answer.next.next.val == 9
    assert answer.next.next.next.val == 9
    assert answer.next.next.next.next.val == 0
    assert answer.next.next.next.next.next.val == 0
    assert answer.next.next.next.next.next.next.val == 0
    assert answer.next.next.next.next.next.next.next.val == 1
    assert answer.next.next.next.next.next.next.next.next is None
    print('\nTests done\n')