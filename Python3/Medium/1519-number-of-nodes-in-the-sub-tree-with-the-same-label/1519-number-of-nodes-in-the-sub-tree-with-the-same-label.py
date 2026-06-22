class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        matrix = {i: [] for i in range(n)}

        for u, v in edges:
            matrix[u].append(v)
            matrix[v].append(u)

        def dfs(node, parent):
            freq = {}
            if labels[node] not in freq:
                freq[labels[node]] = 0
            freq[labels[node]] += 1

            for child in matrix.get(node, []):
                if child == parent:
                    continue

                element_from_child = dfs(child, node)

                for key, value in element_from_child.items():
                    freq[key] = freq.get(key, 0) + value

            ans[node] = freq[labels[node]]
            return freq

        ans = [0] * n
        dfs(0, -1)
        return ans
