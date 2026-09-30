class Solution:#p1, p2, p3 are picked in index order
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()#help prevent dups
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1#returns 0 if not available

        res = []
        for i in range(len(nums)):

            p1 = nums[i]#decrease the count
            counts[p1] -= 1#means that it is a potential candidate, prevent duplicate use
            #always decrement it 
            if i > 0 and nums[i] == nums[i-1]:#short circuiting
                continue
           

            for j in range(i + 1, len(nums)):
                p2 = nums[j]
                counts[p2] -= 1#decrement before because its a potential candidate. If it is a dupe, it doesnt matter


                if j > i + 1 and nums[j] == nums[j-1]:#skip duplicate p2 values
                    continue

                p3 = -(p2 + p1)#not exacttly a 3rd pointer
                if counts.get(p3, 0) > 0: #check for the other exists
                    res.append([p1, p2, p3])

            for j in range(i + 1, len(nums)): counts[nums[j]] += 1#need to restore counts

        return res

class Solution:#numbers that sum together move inward
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()#in place
        res = []
        for i, p1 in enumerate(nums):
            if p1 > 0: break#sorted order so if already positive, cannot continue
            if i > 0 and nums[i] == nums[i-1]: continue#dup from a previous pass

            p2 = i + 1#1 after i. not actually aaccessing index
            p3 = len(nums) - 1 #last element
            while p2 < p3:
                total = p1 + nums[p2] + nums[p3]
                if total > 0:
                    p3 -= 1
                elif total < 0:
                    p2 += 1
                else: 
                    res.append([p1, nums[p2], nums[p3]])
                    p2 += 1
                    p3 -= 1
                #skipping dups only until find valid answer. Then you can skip (helps prevent out of bounds)
                    while p2 < p3 and nums[p2] == nums[p2 - 1]:
                        p2 += 1

                    while p2 < p3 and nums[p3] == nums[p3 + 1]:
                        p3 -= 1

        return res

                

            


                
                




