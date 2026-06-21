class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        matrix = {i: [] for i in range(n)}

        def find_dist(p1, p2):
            x1 = p1[0]
            y1 = p1[1]
            x2 = p2[0]
            y2 = p2[1]

            return abs(x1 - x2) + abs(y1 - y2)

        for i, edge_1 in enumerate(points):
            for j, edge_2 in enumerate(points):
                if i != j:
                    matrix[i].append((j, find_dist(edge_1, edge_2)))
        
        distance = [float('inf')] * n
        distance[0] = 0

        visited = set()

        heap = [(0, 0)]
        while heap:
            curr_dist, curr_node = heapq.heappop(heap)

            if curr_node in visited:
                continue

            visited.add(curr_node)

            for nei_node, nei_dist in matrix.get(curr_node, []):
                if nei_node not in visited:
                    if distance[nei_node] > nei_dist:
                        distance[nei_node] = nei_dist
                        heapq.heappush(heap, (nei_dist, nei_node))

        return sum(distance)
