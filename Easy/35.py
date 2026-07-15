class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        bottom = 0
        top = len(nums) - 1#just in case it needs to go after
        while (top >= bottom):#do one more so bottom can take the up
            mid = (top + bottom) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:#middle index is less than the target so you need to search right
                bottom = mid + 1
            else: #nums[mid] > target, need to search left
                top = mid - 1
        
        return bottom
        
        