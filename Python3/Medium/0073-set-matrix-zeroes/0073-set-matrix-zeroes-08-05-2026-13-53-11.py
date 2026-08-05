class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        firstRowZero = False
        firstColZero = False
        
        for i in range(m):
            if matrix[i][0] == 0:
                firstRowZero = True
                break
            
        for j in range(n):
            if matrix[0][j] == 0:
                firstColZero = True
                break
        
        for i in range(1, m):
            for j in range(1, n):

                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        

        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if firstRowZero:
            for i in range(m):
                matrix[i][0] = 0
        
        if firstColZero:
            for j in range(n):
                matrix[0][j] = 0
        
        
