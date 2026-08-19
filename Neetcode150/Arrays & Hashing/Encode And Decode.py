class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(str(len(strs[i])) + "#" + strs[i] for i in range(len(strs)))
        # this returns a list of strings return [str(len(strs[i])) + "#" + strs[i] for i in range(len(strs))]


    def decode(self, s: str) -> List[str]:#starts with digits#stringdigits#
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])#need to cut off 1 before j because j will be incremented prior. need to convert into int
            result.append(s[j + 1: j + 1 + length])#first character begins on + 1.
            i = j + 1 + length#need to move 1 beyond
        
        return result