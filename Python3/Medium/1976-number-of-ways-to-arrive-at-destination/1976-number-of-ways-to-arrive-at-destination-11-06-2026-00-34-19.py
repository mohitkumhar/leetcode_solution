class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:

        matrix = {i: [] for i in range(n)}

        MOD = 10**9 + 7

        for u, v, w in roads:
            matrix[u].append((v, w))
            matrix[v].append((u, w))

        distance = [float("inf")] * n
        count = [0] * n

        distance[0] = 0
        count[0] = 1

        heap = [(0, 0)]

        while heap:
            currCost, node = heapq.heappop(heap)

            if currCost > distance[node]:
                continue

            for child, cost in matrix.get(node, []):

                newCost = currCost + cost

                if newCost < distance[child]:
                    distance[child] = newCost
                    count[child] = count[node]

                    heapq.heappush(heap, (newCost, child))

                elif newCost == distance[child]:
                    count[child] = (count[child] + count[node]) % MOD

        return count[n - 1]
