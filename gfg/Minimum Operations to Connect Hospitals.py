class Solution:
    def minConnect(self, V, edges):
        total_edges = len(edges)

        if total_edges < (V - 1):
            return -1


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

        for edge in edges:
            a = edge[0]
            b = edge[1]

            union(a, b)


        components = len({find(i) for i in range(V)})

        return components - 1
        
