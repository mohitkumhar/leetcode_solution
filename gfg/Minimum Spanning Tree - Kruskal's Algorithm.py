import heapq

from typing import List

class Solution:
    def kruskalsMST(self, V: int, edges: List[List[int]]) -> int:
        
        matrix = {i: [] for i in range(V)}
        visited= set()
        for u, v, w in edges:
            matrix[u].append((v, w))
            matrix[v].append((u, w))

        parent = [-1] * V
        distance = [float('inf')] * V
        distance[0] = 0

        heap = [(0, 0, -1)]
        
        total_dist = 0
        
        while heap:
            dist, node, parent = heapq.heappop(heap)
            if node in visited:
                continue

            total_dist += dist
            if node not in visited:
                visited.add(node)
            
            for nei_node, weight in matrix.get(node, []):
                if nei_node not in visited:
                    if distance[nei_node] > weight:
                        distance[nei_node] = weight
                
                        heapq.heappush(heap, (weight, nei_node, parent))
        
        return total_dist

            
