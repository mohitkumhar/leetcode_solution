class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        grid = [[0] * n for _ in range(n)] 

        top = 0
        bottom = n - 1

        left = 0
        right = n - 1
        num = 1


        while left <= right and top <= bottom:
            # top (left -> right)
            for i in range(left, right + 1):
                grid[top][i] = num
                num += 1
            top += 1

            # right (top -> bottom)
            for i in range(top, bottom + 1):
                grid[i][right] = num
                num += 1
            right -= 1

            # bottom (right -> left)
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    grid[bottom][i] = num
                    num += 1
                bottom -= 1

            # left (bottom -> top)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    grid[i][left] = num
                    num += 1
                left += 1

        return grid

