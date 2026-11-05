class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:

        matrix = {i: [] for i in range(n)}

        for u, v, cost in flights:
            matrix[u].append((v, cost))

        distance = [float("inf")] * n
        distance[src] = 0

        stops = 0
        queue = [(src, 0)]

        while queue:
            if stops == (k + 1):
                break

            for _ in range(len(queue)):
                node, cost = queue.pop(0)

                for nei, currCost in matrix[node]:
                    if (cost + currCost) < distance[nei]:
                        distance[nei] = cost + currCost
                        queue.append((nei, cost + currCost))

            stops += 1

        return distance[dst] if distance[dst] != float("inf") else -1
