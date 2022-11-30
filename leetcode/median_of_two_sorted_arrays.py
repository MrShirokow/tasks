"""
https://leetcode.com/problems/median-of-two-sorted-arrays/
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # для удобства делаем так, что m <= n
        m = len(nums1)
        n = len(nums2)

        # два указателя
        start = 0
        end = m

        while start <= end:
            # индексы разбивки массивов
            partition_nums1 = (start + end) // 2
            partition_nums2 = (n + m + 1) // 2 - partition_nums1

            # обработка случаев, когда индекс разбиения - это крайний индекс
            max_left_nums1 = float('-inf') if partition_nums1 == 0 else nums1[partition_nums1 - 1]
            min_right_nums1 = float('+inf') if partition_nums1 == m else nums1[partition_nums1]
            max_left_nums2 = float('-inf') if partition_nums2 == 0 else nums2[partition_nums2 - 1]
            min_right_nums2 = float('+inf') if partition_nums2 == n else nums2[partition_nums2]

            # Проверяем пересечение (как с прямоугольниками)
            if max_left_nums1 <= min_right_nums2 and max_left_nums2 <= min_right_nums1:
                if (n + m) % 2 == 0:
                    return (max(max_left_nums1, max_left_nums2) + min(min_right_nums1, min_right_nums2)) / 2
                return max(max_left_nums1, max_left_nums2)
            # иначе сдвигаем указатели
            elif max_left_nums1 > min_right_nums2:
                end = partition_nums1 - 1
            else:
                start = partition_nums1 + 1


if __name__ == '__main__':
    solution = Solution()
    assert solution.findMedianSortedArrays([1,3], [2]) == 2.0
    assert solution.findMedianSortedArrays([1,2], [3, 4]) == 2.5
    assert solution.findMedianSortedArrays([1,3], [2, 7]) == 2.5
    print('\nTests done\n')