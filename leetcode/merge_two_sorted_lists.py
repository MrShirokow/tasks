"""
https://leetcode.com/problems/merge-two-sorted-lists/
"""


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current = result = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1, current = list1.next, list1
            else:
                current.next = list2
                list2, current = list2.next, list2
        current.next = list1 or list2
        return result.next


if __name__ == '__main__':
    solution = Solution()
    answer = solution.mergeTwoLists(
        ListNode(1, 
            ListNode(2, 
                ListNode(4)
            )
        ),
        ListNode(1, 
            ListNode(3, 
                ListNode(4)
            )
        ),
    )
    assert answer.val == 1
    assert answer.next.val == 1
    assert answer.next.next.val == 2
    assert answer.next.next.next.val == 3
    assert answer.next.next.next.next.val == 4
    assert answer.next.next.next.next.next.val == 4
    assert answer.next.next.next.next.next.next is None
    print('\nTests done\n')
