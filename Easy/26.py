class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        for item in nums:
            if item in seen:
                nums.remove(item)
            else:
                seen.add(item)
        
        return len(nums)\

#%%

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0# starat both pointers at zero they hold the index
        for i, num in enumerate(nums):#we need the indexes and values. i corresponds to p2
            if (nums[p1] != num):#if the current value is unique from the end of the sorted portion
                for j in reversed(range(p1 + 2, i + 1)):#start swapping backwards, perform a right shift basically. 
                    #couldve also used range(i, p1 + 1, -1), in this case i is the start boundary
                    #reversed(range(2, 0)) returns 1, 0
                    temp = nums[j - 1]#hold the previous value
                    nums[j - 1] = nums[j]#previous value takes the old
                    nums[j] = temp#old takes the previous
                p1 += 1#advance the pointer foward by 1
        
        return p1 + 1#this is the number of unique elements, length

#%%
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0#index of the last unique element
        p2 = 0
        for i in range(len(nums)):
            if nums[p1] != nums[p2]:#if the 2 values are unique, p1 and p2 are not necessarily right next to each otehr
                temp = nums[p1 + 1]#the element after p1 which is the last unique elemnt gets overwritten
                nums[p1 + 1] = nums[p2]
                nums[p2] = temp
                p1 += 1
            
            p2 += 1
        
        return p1 + 1#non empty
