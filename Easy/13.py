"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

"""

class Solution:
    def romanToInt(self, s: str) -> int:
        lib = {#keys can be tuples, not lkists
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        total = 0
        for i in range(len(s) - 1): #need to compare with indexes, end one before
            curr_val = lib[s[i]]
            next_val = lib[s[i + 1]]

            if  curr_val < next_val:
                total -= curr_val
            else:
                total += curr_val
        return total + lib[s[-1]]#just add the last value