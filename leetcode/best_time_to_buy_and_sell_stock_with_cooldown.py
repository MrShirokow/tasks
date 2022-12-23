"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
"""


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        previous_sell = 0
        previous_cooldown = 0
        previous_buy = -prices[0]

        for price in prices[1:]:
            buy = max(previous_cooldown - price, previous_buy)
            sell = max(previous_buy + price, previous_sell)
            previous_buy = buy
            previous_cooldown = previous_sell
            previous_sell = sell

        return max((previous_cooldown, previous_sell))


if __name__ == '__main__':
    solution = Solution()
    assert solution.maxProfit([1,2,3,0,2]) == 3
    assert solution.maxProfit([1]) == 0
    print('\nTests done\n')
