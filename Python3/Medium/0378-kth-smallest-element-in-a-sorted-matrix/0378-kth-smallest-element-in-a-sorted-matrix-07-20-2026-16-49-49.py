class Solution:

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        def find_smaller_element(val):
            i = n - 1
            j = 0
            count = 0

            while i >= 0 and j < n:
                if matrix[i][j] <= val:
                    count += i + 1
                    j += 1
                else:
                    i -= 1

            return count

        n = len(matrix)

        # smallest val
        left = matrix[0][0]

        # largest val
        right = matrix[n - 1][n - 1]

        while left < right:
            mid = left + (right - left) // 2
            smaller_element = find_smaller_element(mid)

            if smaller_element >= k:
                right = mid
            else:
                left = mid + 1

        return left
