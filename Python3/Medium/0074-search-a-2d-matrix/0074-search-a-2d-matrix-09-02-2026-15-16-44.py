class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows - 1

        while left <= right:
            mid = left + (right - left) // 2

            if matrix[mid][0] <= target <= matrix[mid][cols - 1]:
                l = 0
                r = cols - 1

                while l <= r:
                    m = l + (r - l) // 2

                    if matrix[mid][m] == target:
                        return True

                    elif matrix[mid][m] < target:
                        l = m + 1
                    else:
                        r = m - 1
                return False

            elif target < matrix[mid][0]:
                right = mid - 1
            else:
                left = mid + 1

        return False
