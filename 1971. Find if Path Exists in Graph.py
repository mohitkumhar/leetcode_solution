class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        matrix = {}

        for u, v in edges:
            if u not in matrix:
                matrix[u] = []
            if v not in matrix:
                matrix[v] = []

            matrix[u].append(v)
            matrix[v].append(u)

        queue = [source]
        visited = [False] * n
        visited[source] = True

        while queue:
            curr = queue.pop(0)
            if curr == destination:
                return True

            for next_node in matrix[curr]:
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)

        return False
