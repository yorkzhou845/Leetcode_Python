class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            triangle.append([])
            for j in range(i + 1):#need plus 1 because range is exclusive
                if j == i or j == 0: triangle[i].append(1)
                elif i > 1: triangle[i].append(triangle[i - 1][j - 1] + triangle[i - 1][j])


        return triangle


import math
class Solution:#math
    def comb(self, n: int, r: int) -> int:
        return int(math.factorial(n) / (math.factorial(n - r) * math.factorial(r)))#must cast to int because division by default returnf float
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            triangle.append([])
            for j in range(i + 1):#need plus 1 because range is exclusive
                if i == 0: #the first is 1C1
                    triangle[i].append(self.comb(1, 1))
                else:
                    triangle[i].append(self.comb(i, j))
    
    
        return triangle
