class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        result = []
        n = len(graph)

        def dfs(node, src, dst, path):
            if node == dst:
                result.append(path[:])

            for nei in graph[node]:
                path.append(nei)
                dfs(nei, src, dst, path)
                path.pop()

        dfs(0, 0, n-1, [0])
        return result