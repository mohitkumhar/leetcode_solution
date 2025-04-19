class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row, col = len(matrix), len(matrix[0])
        left, right = 0, row * col - 1

        while left <= right:
            mid = (left + right) // 2
            mid_value = matrix[mid // col][mid % col]

            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
