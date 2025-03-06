class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        j = 0
        n = len(grid)
        duplicate = 0


        expected_values = set(range(1, n * n + 1))
        print(expected_values)

        for g in grid:
            for i in g:
                if i in seen:
                    duplicate=i
                seen.add(i)
        
        return [duplicate, list(expected_values - seen)[0]]