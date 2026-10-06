class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        n = len(matrix)
        m = len(matrix[0])

        if n == 0:
            return
        rowZero = False
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0: 
                    matrix[0][j] = 0 # mark the first row column as 0
                
                    if i > 0:
                        matrix[i][0] = 0 # mark the first column row as 0
                    else:
                        rowZero = True # if the first row has 0 we want to not store/mark this as well as we wont know it came from the row or column and lose any elements on the first row that were already 0

        for i in range(1,n): # inner matrix starting from 1 row and 1 column
            for j in range(1,m):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0 # check the row or column and mark this element 0
            
        if matrix[0][0] == 0: # handle the first row
            for i in range(n):
                matrix[i][0] = 0 
        
        if rowZero:
            for j in range(0, m):
                matrix[0][j] = 0

        return
        

            