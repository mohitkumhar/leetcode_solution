class Solution:
    def spanningTree(self, V, edges):
        edges.sort(key=lambda x: x[2])
        
        def find(target):
            if target == parent[target]:
                return target
            else:
                parent[target] = find(parent[target])
                return parent[target]

        def union(a, b):
            a_parent = find(a)
            b_parent = find(b)
            
            if a_parent != b_parent:
                parent[b_parent] = a_parent

        parent = [i for i in range(V)]
        weight_sum = 0

        for u, v, w in edges:
            if find(u) != find(v):
                union(u, v)
                weight_sum += w
            
        return weight_sum
