class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            if target - nums[i] not in seen: seen[nums[i]] = i #if the conjugate has not been previosuly added, add itself so in the future its conjugate can find it
            else: return [seen[target - nums[i]], i]#looping form the beginnign so the smaller index will have already been in seen
        return []
        