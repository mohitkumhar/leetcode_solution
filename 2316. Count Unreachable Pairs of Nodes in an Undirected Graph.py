class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def find(target):
            if target == parent[target]:
                return target
            else:
                parent[target] = find(parent[target])
                return parent[target]

        def union(a, b):
            a_parent = find(a)
            b_parent = find(b)

            parent[b_parent] = a_parent

        parent = [i for i in range(n)]
        for edge in edges:
            a = edge[0]
            b = edge[1]

            union(a, b)

        freq = {}

        temp = [find(i) for i in range(n)]

        for value in parent:
            freq[value] = freq.get(value, 0) + 1

        total_nodes = n
        result = 0

        for key, value in freq.items():
            result += value * (total_nodes - value)

            total_nodes -= value

        return result
