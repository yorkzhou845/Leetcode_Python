class Solution:#too inefficient
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = p1 + 1#cannot be equal
        while p1 < len(numbers):
            while p2 < len(numbers):#p2 scans ahead
                if numbers[p2] + numbers[p1] == target: return [1 + p1, 1 + p2]
                p2 += 1#need to increment
            p1 += 1
            p2 = p1 + 1

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1
        while p1 < len(numbers):
            if numbers[p1] + numbers[p2] == target: return [1 + p1, 1 + p2]
            elif numbers[p2] < target - numbers[p1]: p1 += 1#p2 stay at the same place since p1 is getting larger, p2 must be the same or slightly less to satisfy condition
            else: p2 -= 1

        
        


        

