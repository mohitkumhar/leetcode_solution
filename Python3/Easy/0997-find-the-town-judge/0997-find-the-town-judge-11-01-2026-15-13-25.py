class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:

        inDegree = [0] * (n + 1)

        for u, v in trust:
            inDegree[u] -= 1
            inDegree[v] += 1

        for i in range(1, n + 1):
            if inDegree[i] == n - 1:
                return i
        return -1
