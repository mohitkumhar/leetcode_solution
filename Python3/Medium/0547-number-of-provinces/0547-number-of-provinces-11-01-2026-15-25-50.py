class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        matrix = {}

        n = len(isConnected)

        for i in range(n):
            matrix[i] = []

            for j in range(n):
                if isConnected[i][j] == 1:
                    matrix[i].append(j)

        count = 0
        seen = set()

        for i in range(n):
            if i not in seen:
                queue = [i]
                seen.add(i)

                while queue:
                    u = queue.pop(0)

                    for v in matrix.get(u, []):
                        if v not in seen:
                            seen.add(v)
                            queue.append(v)

                count += 1

        return count
