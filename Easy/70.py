class Solution:#very inneficient use memoization below
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

class Solution:#prevents many claculatiosn of the same term
    def climbStairs(self, n: int) -> int:
        lib = {}

        def helper(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in lib:
                return lib[n]#lib is still in the scope
            
            lib[n] = helper(n - 1) + helper(n - 2)#call helper
            return lib[n]
        
        return helper(n)
        
        