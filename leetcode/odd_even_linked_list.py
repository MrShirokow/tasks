"""
https://leetcode.com/problems/odd-even-linked-list/
"""


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        odd, even = head, head.next
        while even and even.next:
            temp = even.next
            even.next = even.next.next
            temp.next = odd.next
            odd.next = temp
            odd, even = odd.next, even.next
        return head

'''
1: 
    head = [2, 1, 3, 5, 6, 4, 7]
    temp = 3
    even.next = 5 (1 -> 5)
    temp.next = 1 (3 -> 1)
    odd.next = 3 (2 -> 3)
    odd, even = 3, 5

2:
    head = [2, 3, 1, 5, 6, 4, 7]
    temp = 6
    even.next = 4 (5 -> 4)
    temp.next = 1 (6 -> 1)
    odd.next = 6 (3 -> 6)
    odd, even = 6, 4
3:
    head = [2, 3, 6, 1, 5, 4, 7]
    temp = 7
    even.next = None (4 -> None)
    temp.next = 1 (7 -> 1)
    odd.next = 7 (6 -> 7)
    odd, even = 7, None

head = [2, 3, 6, 7, 1, 5, 4]
'''

if __name__ == '__main__':
    solution = Solution()
    answer = solution.oddEvenList(
        ListNode(1, 
            ListNode(2, 
                ListNode(3,
                    ListNode(4,
                        ListNode(5)
                    )
                )
            )
        )
    )
    assert answer.val == 1
    assert answer.next.val == 3
    assert answer.next.next.val == 5
    assert answer.next.next.next.val == 2
    assert answer.next.next.next.next.val == 4
    assert answer.next.next.next.next.next is None
    answer = solution.oddEvenList(
        ListNode(2, 
            ListNode(1, 
                ListNode(3, 
                    ListNode(5, 
                        ListNode(6, 
                            ListNode(4,
                                ListNode(7)
                            )
                        )
                    )
                )
            )
        )
    )
    assert answer.val == 2
    assert answer.next.val == 3
    assert answer.next.next.val == 6
    assert answer.next.next.next.val == 7
    assert answer.next.next.next.next.val == 1
    assert answer.next.next.next.next.next.val == 5
    assert answer.next.next.next.next.next.next.val == 4
    assert answer.next.next.next.next.next.next.next is None
    print('\nTests done\n')
