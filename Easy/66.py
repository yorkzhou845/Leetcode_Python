class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1#add the last digit
        for i in range(len(digits) - 1, 0, -1):#start at end at 1. Cannot go beyond or else risk out of bounds. The stop value is nvr included
            if digits[i] >= 10:#carry
                digits[i - 1] += 1
                digits[i] -= 10#carried
        
        if digits[0] >= 10:#handle the first digit
            digits[0] -= 10
            digits.insert(0, 1)
        
        return digits
            
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(x) for x in str((int("".join(str(y) for y in digits)) + 1))]
    
class Solution:
    plusOne = lambda self, digits: [int(x) for x in str((int("".join(str(y) for y in digits)) + 1))]
    
