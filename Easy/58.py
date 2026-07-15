class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

import string

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        p1 = len(s) - 1 #index of last character
        while (s[p1] == " "):
            p1 -= 1

        p2 = p1

        while p1 >= 0 and s[p1].isalpha():
            p1 -= 1
        
        
        return p2 - p1
    


    

