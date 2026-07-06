class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        matrix = {i: [] for i in range(1, n + 1)}

        for u, v, w in roads:
            matrix[u].append((v, w))
            matrix[v].append((u, w))

        min_score = float('inf')
        queue = deque([1])
        visited = {1}

        while queue:
            node = queue.popleft()

            for v, w in matrix.get(node, []):
                min_score = min(min_score, w)
                if v not in visited:
                    queue.append(v)
                    visited.add(v)

        return min_score
