class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:

        connected = set()
        inDegree = [0] * n

        for u, v in roads:
            connected.add((u, v))
            connected.add((v, u))

            inDegree[u] += 1
            inDegree[v] += 1

        ans = 0

        for i in range(n):
            for j in range(i + 1, n):

                rank = inDegree[i] + inDegree[j]

                if (i, j) in connected:
                    rank -= 1

                ans = max(ans, rank)

        return ans
