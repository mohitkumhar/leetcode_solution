class Solution:
    def isBipartite(self, V, edges):
        
        matrix = {i: [] for i in range(V)}
        
        for edge in edges:
            matrix[edge[0]].append(edge[1])
            matrix[edge[1]].append(edge[0])

        colors = {}
        
        for start in range(V):
            if start not in colors:
                queue = [(start, 1)]
                colors[start] = 1
                
                while queue:
                    node, curr_color = queue.pop(0)
                    
                    for nei in matrix[node]:
                        if nei in colors and colors[nei] == curr_color:
                            return False
                            
                        elif nei not in colors:
                            queue.append((nei, -curr_color))
                            colors[nei] = -curr_color
        
        return True
        
        
        
