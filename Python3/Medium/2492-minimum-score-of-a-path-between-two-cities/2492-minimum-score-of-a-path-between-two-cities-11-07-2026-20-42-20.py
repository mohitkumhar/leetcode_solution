class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        matrix = {i: [] for i in range(n)}

        for u, v, w in roads:
            if u not in matrix:
                matrix[u] = []
            if v not in matrix:
                matrix[v] = []

            matrix[u].append((v, w))
            matrix[v].append((u, w))

        minCost = float("inf")
        queue = [1]
        visited = {1}

        while queue:
            node = queue.pop(0)

            for nei, cost in matrix.get(node, []):
                minCost = min(minCost, cost)
                if nei not in visited:
                    visited.add(nei)

                    minCost = min(minCost, cost)
                    queue.append(nei)

        return minCost
