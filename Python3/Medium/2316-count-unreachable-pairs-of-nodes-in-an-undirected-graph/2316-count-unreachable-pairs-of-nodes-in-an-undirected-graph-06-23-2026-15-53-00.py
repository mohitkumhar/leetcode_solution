class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        matrix = {i: [] for i in range(n)}

        for u, v in edges:
            matrix[u].append(v)
            matrix[v].append(u)

        parent = [i for i in range(n)]
        visited = set()

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

        for start in range(n):
            if start in visited:
                continue

            queue = deque([start])
            while queue:
                node = queue.popleft()
                if node in visited:
                    continue
                visited.add(node)

                for nei in matrix.get(node, []):
                    if nei not in visited:
                        if find(node) != find(nei):
                            union(node, nei)
                        queue.append(nei)

        freq = {}
        for ele in parent:
            freq[ele] = freq.get(ele, 0) + 1

        result = 0
        total_nodes = n
        for element, size in freq.items():
            result += (size * (total_nodes - size))

            total_nodes -= size

        return result
