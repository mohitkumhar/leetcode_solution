import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        matrix = {i: [] for i in range(n + 1)}


        for u, v, w in times:
            matrix[u].append((v, w))

        print(matrix)
        distance = [float('inf')] * (n + 1)

        distance[k] = 0

        heap = [(0, k)]

        while heap:
            curr_dist, node = heapq.heappop(heap)

            if curr_dist > distance[node]:
                continue

            for nei_node, dist in matrix[node]:
                new_dist = curr_dist + dist

                if new_dist < distance[nei_node]:
                    distance[nei_node] = new_dist
                    heapq.heappush(heap, (new_dist, nei_node))

        return max(distance[1:]) if max(distance[1:]) != float('inf') else -1
