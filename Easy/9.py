class Solution:
    def isPalindrome(self, x: int) -> bool:
        start = 0
        end = len(str(x)) - 1#cannot use len on just x
        while (start <= end):
            if (str(x)[start] != str(x)[end]):
                return False
            else:
                start += 1
                end -= 1
        return True
    
#%%

import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):#account for negative numberss
            return False
        
        while (x > 9):#the last one digit number accounting for odd numbers
            magnitude = int(math.log10(x))#use int decimal trimming to round down, does not work if there are zeros inside
            first_digit = x // 10 ** magnitude #// rounds down
            last_digit = x % 10
            if (first_digit != last_digit):
                return False
            else:
                x = x - first_digit * 10 ** magnitude - last_digit * 10
        
        return True

#%%

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        original = x
        reversed = 0
        while (x > 0):
            digit = x % 10
            reversed = 10 * reversed + digit#multiply the previous digit by 10 to built it backward
            x //= 10 #cut the last digit out
        return reversed == original
            