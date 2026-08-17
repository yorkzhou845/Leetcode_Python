class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        digit = 0
        for i, val in enumerate(nums):
            digit = digit ^ val
        
        return digit
        