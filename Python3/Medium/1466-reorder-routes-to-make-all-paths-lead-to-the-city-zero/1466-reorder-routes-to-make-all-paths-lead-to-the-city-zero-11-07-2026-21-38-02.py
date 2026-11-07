class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:

        matrix = {i: [] for i in range(n)}
        direction = {i: [] for i in range(n)}

        for u, v in connections:
            matrix[u].append(v)
            matrix[v].append(u)

            direction[u].append(v)

        queue = deque([0])
        visited = {0}
        count = 0

        while queue:
            node = queue.popleft()

            for nei in matrix[node]:
                if nei not in visited:
                    if nei in direction[node]:
                        count += 1
                    visited.add(nei)
                    queue.append(nei)
        return count
