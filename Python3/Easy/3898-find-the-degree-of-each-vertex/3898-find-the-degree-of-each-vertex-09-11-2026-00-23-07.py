class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ans = []

        for mat in matrix:
            degree = 0

            for num in mat:
                if num == 1:
                    degree += 1

            ans.append(degree)
        return ans
