class Solution:
    def validPath(
        self, n: int, edges: list[list[int]], source: int, destination: int
    ) -> bool:

        matrix = {}

        for u, v in edges:
            if u not in matrix:
                matrix[u] = []
            if v not in matrix:
                matrix[v] = []

            matrix[u].append(v)
            matrix[v].append(u)

        seen = set()

        queue = [source]
        seen.add(source)

        while queue:
            node = queue.pop(0)

            if node == destination:
                return True

            for v in matrix.get(node, []):
                if v not in seen:
                    seen.add(v)
                    queue.append(v)

        return False
