class Solution:#T: O(NLogN); S: O(N)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}#key val = digit freq
        for num in nums:
            if num in table: table[num] += 1
            else: table[num] = 1
        
        descending = sorted(table.items(), key = lambda key: key[1], reverse = True)#use the keys to sort in descending order
        return [descending[i][0] for i in range(k)]#do not need the entire tuple, just the vals

class Solution:#use bucket sort where the index represents the frequency
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashtable = {}#key val = digit freq
        for num in nums:
            if num in hashtable: hashtable[num] += 1
            else: hashtable[num] = 1
        buckets = [[] for _ in range(len(nums) + 1)]#create all necessary buckets (can have at most len(nums) frequency if all the same. need +1 because exclusive)     
        for key, val in hashtable.items():
            buckets[val].append(key)

        result = []
        for freq in range(len(buckets) - 1, 0, -1):#start at the highest possible frequency
            for num in buckets[freq]:
                result.append(num)

                if len(result) == k: return result #k >= 1


"""
        final = [item for sublist in buckets for item in sublist]#like neted loop to flatten
        return final[-k:] if k != 0 else [] #if k = 0, then the entire thing would be returned
"""

        

        