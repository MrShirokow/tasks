"""
https://leetcode.com/problems/keys-and-rooms/
"""

from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return False
        stack = [0]
        visited = [False] * len(rooms)
        visited[0] = True
        while stack:
            for key in rooms[stack.pop()]:
                if not visited[key]:
                    visited[key] = True
                    stack.append(key)
        for state in visited:
            if not state:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    assert solution.canVisitAllRooms([[1],[2],[3],[]])
    assert not solution.canVisitAllRooms([[1,3],[3,0,1],[2],[0]])
    print('\nTests done\n')
