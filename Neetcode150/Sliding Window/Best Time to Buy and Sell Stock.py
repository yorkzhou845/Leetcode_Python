class Solution:#Dynamic programing method
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0#currnt max profit
        min_price = prices[0]#the the all tiem min price

        for price in prices:
            new_diff = price - min_price#the current optimal profit from this price
            if new_diff > max_diff: max_diff = new_diff
            if price < min_price: min_price = price#if this current price is less than the global min, use this as the optimal buy point
        
        return 0 if max_diff <= 0 else max_diff#if the profit is <= 0, make no transaction, else return the profit

        