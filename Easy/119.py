import math
class Solution:#math
    def comb(self, n: int, r: int) -> int:
        return int(math.factorial(n) / (math.factorial(n - r) * math.factorial(r)))#must cast to int because division by default returnf float
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []
        for i in range(rowIndex + 1):
            if i == 0: #the first is 1C1
                triangle.append(self.comb(1, 1))
            else:
                triangle.append(self.comb(rowIndex, i))
    
    
        return triangle