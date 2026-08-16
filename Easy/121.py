class Solution:#iterative
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]#set the min price to the first elemtn
        max_diff = 0#the max diff must be >= 0

        for val in prices:
            diff = val - min#difference between current sell price and the min
            if diff < 0: min = val#if the difference is < 0, there is a new min
            elif diff > max_diff: max_diff = diff#if the difference is greater than the previous max, this is the new profit

        return max_diff


class Solution:#recursion
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0

        return 
