class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        queue = deque([(0, [0])])
        result = []
        n = len(graph)

        while queue:
            node, path = queue.popleft()

            if node == n-1:
                result.append(path)
                continue
            
            for nei in graph[node]:
                queue.append((nei, path + [nei]))

        return result
