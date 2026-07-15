class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, val in enumerate (nums):
            complement = target - val
            if complement in seen:
                return [seen[complement], i]#return the older index first
            else:
                seen[val] = i