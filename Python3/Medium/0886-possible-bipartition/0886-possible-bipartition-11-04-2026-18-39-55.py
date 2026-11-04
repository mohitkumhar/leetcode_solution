class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        matrix = {}

        for u, v in dislikes:
            if u not in matrix:
                matrix[u] = []
            if v not in matrix:
                matrix[v] = []
            matrix[u].append(v)
            matrix[v].append(u)

        colors = {0: 1}

        for start in range(1, n + 1):
            if start in colors:
                continue

            queue = [start]
            colors[start] = 1

            while queue:
                node = queue.pop(0)

                for nei in matrix.get(node, []):
                    if nei not in colors:
                        colors[nei] = -colors[node]
                        queue.append(nei)
                    else:
                        if colors[nei] == colors[node]:
                            return False

        return True
