class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        result = []

        for mat in matrix:
            result.extend(mat)
        result.sort()

        return result[k - 1]
