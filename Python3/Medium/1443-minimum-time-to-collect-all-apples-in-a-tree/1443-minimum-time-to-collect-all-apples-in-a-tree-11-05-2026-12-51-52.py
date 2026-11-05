class Solution:
    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        matrix = {}

        for u, v in edges:
            if u not in matrix:
                matrix[u] = []
            if v not in matrix:
                matrix[v] = []
            matrix[u].append(v)
            matrix[v].append(u)

        def dfs(node, parent):
            time = 0

            for child in matrix.get(node, []):
                if child == parent:
                    continue

                timeTakenByChild = dfs(child, node)

                if timeTakenByChild or hasApple[child]:
                    time += 2 + timeTakenByChild

            return time

        return dfs(0, -1)
