class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        matrix = {}
        MOD = 10**9 + 7

        for u, v in edges:
            if u not in matrix:
                matrix[u] = []
            if v not in matrix:
                matrix[v] = []

            matrix[u].append(v)
            matrix[v].append(u)
        
        dep = 0
        queue = [(1, 0)]
        seen = {1}

        while queue:
            node, depth = queue.pop(0)

            dep = max(dep, depth)

            for nei in matrix[node]:
                if nei not in seen:
                    queue.append((nei, depth + 1))
                    seen.add(nei)

        return pow(2, dep - 1, MOD)
