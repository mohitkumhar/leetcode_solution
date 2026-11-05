class Solution:
    def countSubTrees(self, n: int, edges: list[list[int]], labels: str) -> list[int]:

        matrix = {i: [] for i in range(n)}
        answer = [0] * n

        for u, v in edges:
            matrix[u].append(v)
            matrix[v].append(u)

        def dfs(node, parent):
            freq = {}
            freq[labels[node]] = freq.get(labels[node], 0) + 1

            for child in matrix[node]:
                if child == parent:
                    continue

                fetchLabelsFromChild = dfs(child, node)

                for key, value in fetchLabelsFromChild.items():
                    freq[key] = freq.get(key, 0) + value

            answer[node] = freq.get(labels[node], 0)
            return freq

        dfs(0, -1)
        return answer
