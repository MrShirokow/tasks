"""
https://leetcode.com/problems/middle-of-the-linked-list/
"""


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tree = {}
        current = head
        index = 0
        while current:
            tree[index] = current
            current = current.next
            index += 1
        return tree[index // 2]


if __name__ == '__main__':
    solution = Solution()
    answer = solution.middleNode(
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
    assert answer.val == 3
    assert answer.next.val == 4
    assert answer.next.next.val == 5
    assert answer.next.next.next is None
    answer = solution.middleNode(ListNode(0))
    assert answer.val == 0
    assert answer.next is None
    answer = solution.middleNode(
        ListNode(1, 
            ListNode(2, 
                ListNode(3, 
                    ListNode(4, 
                        ListNode(5, 
                            ListNode(6)
                        )
                    )
                )
            )
        )
    )
    assert answer.val == 4
    assert answer.next.val == 5
    assert answer.next.next.val == 6
    assert answer.next.next.next is None
    print('\nTests done\n')
