class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        m = len(mat)
        n = len(mat[0])

        left = 0
        right = m - 1

        while left <= right:
            mid = left + (right - left) // 2

            maxColElementIdx = mat[mid].index(max(mat[mid]))

            top = mat[mid - 1][maxColElementIdx] if mid > 0 else -1
            bottom = mat[mid + 1][maxColElementIdx] if mid < m - 1 else -1

            if mat[mid][maxColElementIdx] > top and mat[mid][maxColElementIdx] > bottom:
                return [mid, maxColElementIdx]

            elif mat[mid][maxColElementIdx] < top:
                right = mid - 1
            else:
                left = mid + 1

        return [-1, -1]
