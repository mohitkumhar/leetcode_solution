class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        matrix = {i: [] for i in range(1, n + 1)}

        for u, v, w in roads:
            matrix[u].append((v, w))
            matrix[v].append((u, w))

        self.min_cost = float('inf')
        visited = set()

        def dfs(u):
            if u in visited:
                return
            visited.add(u)

            for v, w in matrix.get(u, []):
                self.min_cost = min(self.min_cost, w)
                if v not in visited:
                    dfs(v)

        dfs(1)
        return self.min_cost
