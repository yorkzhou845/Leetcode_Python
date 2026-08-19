class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}#at most 26 characters (key value pairs)
        hash2 = {}
        for c in s:
            if c in hash1:
                hash1[c] += 1
            else:
                hash1[c] = 1
        
        for c in t:
            if c in hash2:
                hash2[c] += 1
            else:
                hash2[c] = 1
        
        return hash1 == hash2

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = [0] * 26#serves as a hashtable bscially
        hash2 = [0] * 26
        for c in s:
            hash1[ord(c) - ord('a')] += 1
        
        for c in t:
            hash2[ord(c) - ord('a')] += 1
        
        return hash1 == hash2
        

        

        