class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        seen = set()
        duplicate = 0

        for i in grid:
            for j in i:
                if j in seen:
                    duplicate = j
                else:
                    seen.add(j)

        missingElement = 0

        n = len(grid)
        for i in range(1, n * n + 1):
            if i not in seen:
                missingElement = i

        return [duplicate, missingElement]
