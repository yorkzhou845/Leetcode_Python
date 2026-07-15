class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        p1 = 0
        while (p1 < len(haystack)):
            if needle == haystack[p1: p1 + len(needle)]:#the ast index is already excluded
                return p1
            p1 += 1
        
        return -1