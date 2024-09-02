class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if not m * n == len(original):
            return []

        res = [[None for _ in range(n)] for _ in range(m)]
        index = 0

        for i in range(m):
            for j in range(n):
                res[i][j] = original[index]
                index += 1
        
        return res
        
