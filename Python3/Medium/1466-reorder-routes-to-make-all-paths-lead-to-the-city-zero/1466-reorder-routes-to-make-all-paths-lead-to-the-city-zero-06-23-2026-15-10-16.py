class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        matrix = {i: [] for i in range(n)}
        direction = {i: [] for i in range(n)}

        for u, v in connections:
            matrix[u].append(v)
            matrix[v].append(u)

            direction[u].append(v)

        queue = [0]
        count = 0
        visited = set()

        while queue:
            node = queue.pop(0)
            if node in visited:
                continue
            visited.add(node)

            for nei in matrix.get(node, []):
                if nei not in visited:
                    if nei in direction[node]:
                        count += 1

                    queue.append(nei)

        return count
