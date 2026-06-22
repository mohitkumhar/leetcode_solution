class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        matrix = {i:[] for i in range(n)}
        for u, v in edges:
            matrix[u].append(v)
            matrix[v].append(u)

        queue = deque([source])
        visited = set()

        while queue:
            node = queue.popleft()
            if node == destination:
                return True

            if node in visited:
                continue
            visited.add(node)

            for v in matrix.get(node, []):
                if v not in visited:
                    queue.append(v)

        return False
