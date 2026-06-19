class Solution:
	def isCycle(self, V, edges):


        matrix = {}
        
        for u, v in edges:
            if u not in matrix:
                matrix[u] = []
            if v not  in matrix:
                matrix[v] = []
            
            matrix[u].append(v)
            matrix[v].append(u)
        
        # print(matrix)
        visited = set()
        for start in range(V):
            if start in visited:
                continue
            stack = [(start, -1)]

            while stack:
                node, parent = stack.pop()

                if node in visited:
                    continue
                visited.add(node)

                for nei in matrix.get(node, []):
                    if nei == parent:
                        continue
                    
                    if nei in visited:
                        return True
                    stack.append((nei, node))
        return False
                
