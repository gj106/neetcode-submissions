class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        i = 0
        n = len(matrix)
        m = len(matrix[0])

        if n == 0 or m == 0:
            return False

        j = (n * m) -1 # goto the last element

        while i <= j:
            mid = (i + j)//2

            # calculate the mid indices
            lmid = mid // m # division
            rmid = mid % m # residual
            midval = matrix[lmid][rmid]
            if midval < target:
                i = mid+1
            elif midval > target:
                j = mid-1
            else:
                return True
            
        
        return False
            