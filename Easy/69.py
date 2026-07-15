class Solution:
    def mySqrt(self, x: int) -> int:
        y = 0
        while (y ** 2 <= x):
            y += 1
        
        return y - 1

class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        while (high >= low):#right low will go 1 too high
            mid = (low + high) // 2
            if (mid ** 2 == x):
                return mid
            elif (mid ** 2 < x):#result must be in the upper half then
                low  = mid + 1
            else: #lower half
                high = mid - 1
        
        return high#left will go one higher