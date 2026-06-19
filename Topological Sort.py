class Solution:
    def topoSort(self, V, edges):
        matrix = {i: [] for i in range(V)}
        
        for u, v in edges:
            matrix[u].append(v)
        

        
        def dfs(node):
            visited.add(node)
            
            for nei in matrix[node]:
                if nei not in visited:
                    dfs(nei)
            topo.append(node)
        
        
        visited = set()
        topo = []

        for start in range(V):
            
            if start not in visited:
                dfs(start)

        return topo[::-1]
