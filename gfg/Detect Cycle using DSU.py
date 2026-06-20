class Solution:
	def detectCycle(self, V, adj):
	    rank = [0] * V
        parent = [i for i in range(V)]

        def find(target):
            if target == parent[target]:
                return target
            
            else:
                parent[target] = find(parent[target])
                return parent[target]
                
        	    
		
		def union(a, b):
		    a_parent = find(a)
		    b_parent = find(b)
		    
		    if a_parent == b_parent:
		        return True
		       
		    elif rank[a_parent] > rank[b_parent]:
		        parent[b_parent] = a_parent
		       
		    elif rank[a_parent] < rank[b_parent]:
		        parent[a_parent] = b_parent
		  
		    else:
		        parent[b_parent] = a_parent
		        rank[a_parent] += 1
		  
		    return False
		 
		 
        for u in range(V):
            for v in adj[u]:
                if u < v:
                    if union(u, v):
                        return True
        return False
