class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:

        def dfs(node):
            visited.add(node)

            for nei in matrix[node]:
                if nei not in visited:
                    dfs(nei)

        n = len(stones)
        matrix = {i: [] for i in range(n + 1)}

        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    matrix[i].append(j)
                    matrix[j].append(i)

        visited = set()
        components = 0

        for i, stone in enumerate(stones):
            if i not in visited:
                components += 1
                dfs(i)

        return n - components
