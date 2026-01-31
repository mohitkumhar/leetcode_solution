class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = {}
        for u, v in dislikes:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)

        color = [0] * (n+1)
        queue = []

        for node in graph:
            if color[node] != 0:
                continue
            color[node] = 1
            queue.append(node)

            while queue:
                val = queue.pop(0)

                for nei in graph[val]:
                    if color[nei] == 0:
                        color[nei] = -color[val]
                        queue.append(nei)

                    if color[nei] == color[val]:
                        return False
        return True
