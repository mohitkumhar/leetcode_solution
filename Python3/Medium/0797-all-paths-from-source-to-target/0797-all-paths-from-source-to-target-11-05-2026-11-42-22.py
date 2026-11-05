class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        n = len(graph)
        queue = [(0, [0])]
        result = []

        while queue:
            node, path = queue.pop(0)

            if node == n - 1:
                result.append(path)

            for nei in graph[node]:
                queue.append((nei, path + [nei]))

        return result
