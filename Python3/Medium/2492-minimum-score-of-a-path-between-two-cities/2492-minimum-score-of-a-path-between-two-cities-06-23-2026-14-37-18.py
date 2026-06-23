class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        matrix = {i:[] for i in range(1, n + 1)}

        for u, v, w in roads:
            matrix[u].append((v, w))
            matrix[v].append((u, w))

        self.min_dist = float('inf')
        visited = set()

        def dfs(node):
            if node in visited:
                return 
            visited.add(node)

            for v, w in matrix.get(node, []):
                self.min_dist = min(self.min_dist, w)
                if v not in visited:
                    dfs(v)

        dfs(1)

        return self.min_dist
