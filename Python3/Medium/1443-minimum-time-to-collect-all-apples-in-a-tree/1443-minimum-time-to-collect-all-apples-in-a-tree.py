class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        matrix = {i:[] for i in range(n)}
        for u, v in edges:
            matrix[u].append(v)
            matrix[v].append(u)
        
        def dfs(node, parent):
            time = 0
            
            for child in matrix[node]:
                if child == parent:
                    continue
                time_taken_by_child = dfs(child, node)
            
                if time_taken_by_child > 0 or hasApple[child]:
                    time += (time_taken_by_child + 2)
            return time

        time = dfs(0, -1)

        return time
