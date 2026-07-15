class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        total = 0
        for i,num in enumerate(nums):#if 2 elements are identical, this can stil have vlaues eqaul to val in the front part
            if num == val:
                for j in range(i, len(nums) - 1):#prevent out of bounds
                    temp = nums[j + 1]
                    nums[j + 1] = nums[j]
                    nums[j] = temp
            else:
                total += 1
        return total

#%%

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0#will point the index after the last overwritten value, effectively taking on the length
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            else:#its a good value to overwrite the beginnign part with
                nums[k] = nums[i]
                k += 1
        
        return k
