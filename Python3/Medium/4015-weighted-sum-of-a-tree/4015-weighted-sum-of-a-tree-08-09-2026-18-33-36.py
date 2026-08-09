class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        n = len(parent)

        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        depth = [0] * n

        def dfs(node, d):
            depth[node] = d

            for child in children[node]:
                dfs(child, d + 1)

        dfs(0, 1)

        height = max(depth)

        ans = 0

        for i in range(n):
            ans += nums[i] * (height - depth[i] + 1)

        return ans
