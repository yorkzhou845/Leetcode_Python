class Solution: #space O(1), time O(n^2)
    def trap(self, height: List[int]) -> int:
        left = 0
        right = 0
        total = 0
        while right < len(height) - 1:
            for i in range(right, len(height)):#search until find height[i] > height[left] or the greatest on the right side
                if height[i] >= height[left]:#the moment find something greater or equal, stop scanning
                    right = i
                    break
                elif height[i] > height[right]: right = i#important if there is nothing greater on the right anymore

            small = min(height[left], height[right])#have to use the min of the left and right side for no overflow. Even if the right side has nothing larger than the current, still works
            for i in range(left + 1, right):#iterate through adding on the difference in height. boundaries cannot hold water so must be exclusive on both ends
                total += small - height[i]

            left = right#put everything to the end
            right += 1#need to push the new_max one over or else may be stuck on the same peak

        return total

class Solution:#space O(1), time O(n)
    def trap(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height) - 1
        leftmax = height[p1]
        rightmax = height[p2]
        total = 0
        while p1 < p2:
            if height[p2] > height[p1]: #if the right  wall is taller than the left wall, can safely reel in p1 to the right
                if height[p1] < leftmax:#current value is still lower than the leftmax
                    total += leftmax - height[p1]
                else:#there is a new left max
                    leftmax = height[p1]
                p1 += 1
            else:#left wall is taller than the right wall, can safely bring in p2 to the left
                if height[p2] < rightmax:#current value is lower than the right max
                    total += rightmax - height[p2]
                else:#there is a new right max
                    rightmax = height[p2]
                p2 -= 1

        return total
            
            
                



        

        
                

