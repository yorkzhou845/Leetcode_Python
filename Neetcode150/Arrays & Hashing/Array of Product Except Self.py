class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1#0 holds the product to output for 0s. 1 holds the normal product
        count0 = 0
        for num in nums:#get the total product
            if num != 0: 
                product *= num
            else: count0 += 1 #the digit is a 0
        if count0 >= 2: return [0] * len(nums)#if there are 2 or more 0s, everything is 0
        elif count0 == 1: return [0 if num != 0 else product for num in nums]#exactly one 0
        else: return [product // num for num in nums ]#no 0s


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix = 1#stores the accumlated product from before
        for i in range(len(nums)):
            result[i] *= prefix#only does the stuff from before. Need to multiple and cannot set to 0 just in prefix is 0
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):#2nd bound is awlays excsluvie so need to go to -1
            result[i] *= suffix
            suffix *= nums[i]

        return result
        
