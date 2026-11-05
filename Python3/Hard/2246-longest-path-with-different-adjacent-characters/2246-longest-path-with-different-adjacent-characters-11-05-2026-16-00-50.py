class Solution:
    def longestPath(self, parent: list[int], s: str) -> int:

        def dfs(node, parent):
            nonlocal result

            maxLen1 = 0
            maxLen2 = 0
            currChar = s[node]

            for child in matrix[node]:
                if child == parent:
                    continue

                length = dfs(child, node)

                if s[child] != currChar:

                    if length > maxLen1:
                        maxLen2 = maxLen1
                        maxLen1 = length
                    elif length > maxLen2:
                        maxLen2 = length

            result = max(result, maxLen1 + maxLen2 + 1)
            return maxLen1 + 1

        result = 1

        n = len(parent)

        matrix = {i: [] for i in range(n)}

        for i in range(1, n):
            matrix[parent[i]].append(i)

        dfs(0, -1)
        return result
