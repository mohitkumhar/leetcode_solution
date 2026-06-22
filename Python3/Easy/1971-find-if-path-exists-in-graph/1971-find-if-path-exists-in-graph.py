class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

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

        parent = [i for i in range(n)]
        for u, v in edges:
            if find(u) != find(v):
                union(u, v)
        
        return find(source) == find(destination)
