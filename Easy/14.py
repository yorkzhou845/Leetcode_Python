class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = []
        for i, char in enumerate(strs[0]):#index and character values of the first string
            for val in strs:
                if (i > len(val) - 1 or val[i] != char):
                    return "".join(prefix)#how to make a list into a string
            prefix.append(char)
        
        return "".join(prefix)

#%%
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        for i, char in enumerate(strs[0]):#index and character values of the first string
            for val in strs:
                if (i > len(val) - 1 or val[i] != char):
                    return strs[0][:i]
        
        return strs[0]
    
    


        
    
    


        