class Solution:
    def countConnected(self, V, edges):
        matrix = {i: [] for i in range(V)}

        for u, v in edges:
            matrix[u].append(v)
            matrix[v].append(u)
        
        
        visited = set()
        count = 0
        
        for start in range(V):
            
            if start in visited:
                continue
            
            stack = [start]
            count += 1
            
            while stack:
                node = stack.pop()
                
                if node in visited:
                    continue
                visited.add(node)
                
                for nei in matrix[node]:
                    if nei not in visited:
                        stack.append(nei)
            
        return count

        
