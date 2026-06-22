class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        matrix = {i: [] for i in range(n+1)}

        for u, v in dislikes:
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
                        queue.append((nei))
                        colors[nei] = -colors[node]

                    elif nei in colors:
                        if colors[nei] == colors[node]:
                            return False

        return True
