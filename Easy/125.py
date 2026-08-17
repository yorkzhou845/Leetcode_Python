class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is None: return False
        reversed = []
        for i in range(len(s)): #i will be len - 1 at the end
            if s[len(s) - i - 1].isalpha() or s[len(s) - i - 1].isdigit(): reversed.append(s[len(s) - i - 1].lower())

        cleaned = "".join(c.lower() for c in s if c.isalpha() or c.isdigit())

        return "".join(s for s in reversed) == cleaned#convert list to string

class Solution:#2 pointer
    def isPalindrome(self, s: str) -> bool:
        if s is None: return False
        p1 = 0
        p2 = len(s) - 1
        while (p1 <= p2):
            while p1 < p2 and not s[p1].isalpha() and not s[p1].isdigit(): p1 += 1#need to make sure pointer do not cross prior to checking the rest
            while p1 < p2 and not s[p2].isalpha() and not s[p2].isdigit(): p2 -= 1

            if s[p1].lower() != s[p2].lower(): return False
            p1 += 1
            p2 -= 1

        return True