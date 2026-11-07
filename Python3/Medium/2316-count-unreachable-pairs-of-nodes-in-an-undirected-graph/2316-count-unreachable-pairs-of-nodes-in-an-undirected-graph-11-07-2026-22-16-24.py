class Solution:
    def countPairs(self, n: int, edges: list[list[int]]) -> int:

        def find(target):
            if target == parent[target]:
                return target
            else:
                parent[target] = find(parent[target])
                return parent[target]

        def union(a, b):
            parent_a = find(a)
            parent_b = find(b)

            if parent_a != parent_b:
                parent[parent_b] = parent_a

        matrix = {i: [] for i in range(n)}

        for u, v in edges:
            matrix[u].append(v)
            matrix[v].append(u)

        parent = [i for i in range(n)]
        visited = set()

        for start in range(n):
            if start in visited:
                continue

            queue = [start]
            while queue:
                node = queue.pop(0)

                for nei in matrix[node]:
                    if nei not in visited:
                        visited.add(nei)
                        if find(nei) != find(node):
                            union(node, nei)
                        queue.append(nei)

        freq = {}
        for element in parent:
            freq[element] = freq.get(element, 0) + 1

        count = 0
        totalSize = n

        for key, size in freq.items():

            count += size * (totalSize - size)

            totalSize -= size

        return count
