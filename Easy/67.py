class Solution:
    def addBinary(self, a: str, b: str) -> str:#a and b are binary strings
        s1 = int(a, 2)#convert to base 10 integer from base 2
        s2 = int(b, 2)#will onsider s2 as the carry for now

        while(s2 != 0):#keep adding the shifting bits to the original until the shifts are zero
            sum_withoutCarry = s1 ^ s2#integer representation of the bits no need for carry
            carry = s1 & s2#integer represetation of the bits with carry
            s1 = sum_withoutCarry#need this for the next iteration
            s2 = carry << 1#shift down by 1 to add on the next iteration

class Solution:
    def addBinary(self, a: str, b: str) -> str:#a and b are binary strings
        s1 = int(a, 2)#convert to base 10 integer from base 2
        s2 = int(b, 2)#will onsider s2 as the carry for now

        while(s2 != 0):#keep adding the shifting bits to the original until the shifts are zero
            s1, s2 = s1 ^ s2, (s1 & s2) << 1#tuple assignment
        return bin(s2)
    
class Solution:
    addBinary = lambda self, a, b: bin(int(a, 2) + int(b,2))[2:]

class Solution:
    def addBinary(self, a: str, b: str) -> str:#a and b are binary strings
        result = []
        carry = 0
        for i in range(1, max(len(a), len(b)) + 1):#from 1 to max length because use -1 for reversal. Need + 1
            digit_a = int(a[-i]) if i <= len(a) else 0 #has a digit
            digit_b = int(b[-i]) if i <= len(b) else 0 

            total = digit_a + digit_b + carry#add together
                 
            if sum >= 2:
                    result.insert(0, total - 2)#insert at beginning
                    carry = 1
            else:
                    result.insert(0, total)
                    carry = 0

        
        #deal with the last digit
        if carry == 1:
            result.insert(0, 1)
        
        return "".join(str(x) for x in result)

class Solution:
    def addBinary(self, a: str, b: str) -> str:#a and b are binary strings
        result = []
        carry = 0
        for i in range(1, max(len(a), len(b)) + 1):#from 1 to max length because use -1 for reversal. Need + 1
            digit_a = int(a[-i]) if i <= len(a) else 0 #has a digit
            digit_b = int(b[-i]) if i <= len(b) else 0 

            total = digit_a + digit_b + carry#add together
                 
            result.insert(0, total % 2)#insert at beginning
            carry = total // 2

        
        #deal with the last digit
        if carry == 1:
            result.insert(0, 1)
        
        return "".join(str(x) for x in result)           
