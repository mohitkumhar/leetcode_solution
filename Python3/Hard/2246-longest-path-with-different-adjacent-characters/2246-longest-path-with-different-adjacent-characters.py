class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        matrix = {i: [] for i in range(n)}

        for i in range(1, n):
            matrix[parent[i]].append(i)

        def dfs(node):
            max1 = 0
            max2 = 0

            for child in matrix.get(node, []):
                length = dfs(child)

                if s[child] == s[node]:
                    continue

                if length > max1:
                    max2 = max1
                    max1 = length
                elif length > max2:
                    max2 = length

            self.ans = max(self.ans, max1 + max2 + 1)

            return max1 + 1

        self.ans = 0
        dfs(0)

        return self.ans
        