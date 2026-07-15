class Solution:#do not use insert
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = 0 #for list1
        p2 = 0  #for list2
        inserted = 0#keeps track of how many were inserted
        #p1 always needs to be at the frontier of the already seen portion of nums1 so that p2 can insert into the right spot
        while (p2 < n and p1 < m + inserted):#when p1 excedes, that means reached the zeroes
            if (nums1[p1] == nums2[p2]):
                nums1.insert(p1, nums2[p2])
                p1 += 2
            elif (nums1[p1] > nums2[p2]):
                nums1.insert(p1, nums2[p2])
                p1 += 1#still want to compare the same item
            else: #p1 < p2
                nums1.insert(p1 + 1, nums2[p2])
                p1 += 2#go onto the frontier
            p2 += 1
            inserted += 1
        
        while p2 < n:#tack onto the end
            nums1[p1] = nums2[p2]
            p1 += 1
            p2 += 1
            
        #return up to the 0s at the end
        return nums1[:p1 + 1]

class Solution:#do not use insert
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1#last real position in nums1
        p2 = n - 1#last real position in nums2
        write = m + n - 1# the last slot (last 0)

        while (p1 >= 0 and p2 >= 0):
            if (nums1[p1] >= nums2[p2]):
                nums1[write] = nums1[p1]
                p1 -= 1
            else:#nums[p1] < nums2[p2]
                nums1[write] = nums2[p2]
                p2 -= 1
            write -= 1
        
        #if p2 == 0, then can just return. If p1 == 0 but p2 >= 0, need to writing backwards fro the write
        while (p2 >= 0):
            nums1[write] = nums2[p2]
            
            write -= 1
            p2 -= 1

    