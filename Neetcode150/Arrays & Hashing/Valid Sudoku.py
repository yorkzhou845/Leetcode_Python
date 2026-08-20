class Solution:#could be more than 1 dupe. T: O(n^2). S: O(n)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #can use bucket sort for the rows and col. Need a set for the 3x3 becasue index can no longer be the value becasue the index is coordinates
        for row in range(len(board)):#check rows. Could just use 9 to make it easier
            seen = [False] * 10#the digit will serve as the index and will be false not seen before (0) and true if more than one
            for col in range(len(board[row])):
                if board[row][col] == ".": continue
                curr = int(board[row][col])#the current digit (row then col)
                if not seen[curr]: seen[curr] = True  #the digit has not been seen before
                else: return False
        
        for col in range(9):#check rows
            seen = [False] * 10#the digit will serve as the index and will be false not seen before (0) and true if more than one
            for row in range(9):
                if board[row][col] == ".": continue
                curr = int(board[row][col])#the current digit (col then row)
                if not seen[curr]: seen[curr] = True  #the digit has not been seen before
                else: return False#th 
        
        for i in range(3, 10, 3):#step size 3, rows. need to go all the way up to 9
            for j in range(3, 10, 3):#columns. start at 3
                seen = [False] * 10#moved to the outside becasue care about groups of 3
                for row in range(i - 3, i):#need to do by subjection of 3
                    for col in range(j - 3, j):
                        if board[row][col] == ".": continue
                        curr = int(board[row][col])#the current digit (row then col)
                        if seen[curr]: return False  #the digit has not been seen before
                        else: seen[curr] = True#the
        return True#no False has been thrown so everything was good 


            

                 