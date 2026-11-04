class Solution:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:

        matrix = {i: [] for i in range(n)}

        for u, v in edges:
            matrix[u].append(v)
            matrix[v].append(u)

        count = [1] * n
        answer = [0] * n

        # First DFS: Calculate subtree sizes and root distance sum
        def dfs1(node, parent):
            for nei in matrix[node]:
                if nei != parent:
                    dfs1(nei, node)
                    count[node] += count[nei]
                    answer[node] += answer[nei] + count[nei]

        # Second DFS: Reroot the tree
        def dfs2(node, parent):
            for nei in matrix[node]:
                if nei != parent:
                    answer[nei] = answer[node] + n - 2 * count[nei]
                    dfs2(nei, node)

        dfs1(0, -1)
        dfs2(0, -1)

        return answer
