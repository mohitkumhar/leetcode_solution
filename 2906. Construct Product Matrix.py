class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        prefix_prod = []
        suffix_prod = []
        MOD =  12345
        m = len(grid)
        n = len(grid[0])

        temp_prod = 1
        for i in range(m):
            for j in range(n):
                prefix_prod.append(temp_prod)
                temp_prod = (temp_prod * grid[i][j]) % MOD

        temp_prod = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                suffix_prod.append(temp_prod)
                temp_prod = (temp_prod * grid[i][j]) % MOD


        suffix_prod = suffix_prod[::-1]

        ans = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                idx = i * n + j
                ans[i][j] = (prefix_prod[idx] * suffix_prod[idx]) % 12345

        return ans
