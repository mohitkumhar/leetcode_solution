class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        total_edges = len(connections)

        if total_edges < (n - 1):
            return -1

        parent = [i for i in range(n)]

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

        for connection in connections:
            a = connection[0]
            b = connection[1]

            union(a, b)

        components = len({find(i) for i in range(n)})

        return components - 1
