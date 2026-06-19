class Solution:
    def isCyclic(self, V, edges):
         
        matrix = {i: [] for i in range(V)}
        
        for u, v in edges:
            matrix[u].append(v)
        
        # dfs
        visited = set()
        recursion = set()
        
        
        def dfs(node):
            visited.add(node)
            recursion.add(node)
            
            for nei in matrix.get(node, []):
                if nei not in visited and dfs(nei):
                    return True
                elif nei in recursion:
                    return True
            
            recursion.remove(node)
            return False
                    
        
        for i in range(V):
            if i not in visited:
                if dfs(i):
                    return True
        return False
        
        










