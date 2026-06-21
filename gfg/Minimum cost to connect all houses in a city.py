import heapq
class Solution:
    def minCost(self, houses):

        def find_cost(house1, house2):
            x1, y1 = house1[0], house1[1]
            x2, y2 = house2[0], house2[1]

            return abs(x1 - x2) + abs(y1 - y2)

        n = len(houses)
        matrix = {i: [] for i in range(n)}

        for i, house1 in enumerate(houses):
            for j, house2 in enumerate(houses):
                if i != j:
                    matrix[i].append((j, find_cost(house1, house2)))


        distance = [float('inf')] * n
        distance[0] = 0

        heap = [(0, 0)]
        total_cost = 0
        visited = set()

        while heap:
            curr_cost, u = heapq.heappop(heap)
            if u in visited:
                continue
            visited.add(u)
            total_cost += curr_cost

            for v, nei_cost in matrix[u]:
                if nei_cost < distance[v]:
                    distance[v] = nei_cost
                    heapq.heappush(heap, (nei_cost, v))

        return total_cost
