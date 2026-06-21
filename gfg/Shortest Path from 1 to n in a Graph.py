from typing import List
import heapq

class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        
        matrix = {i: [] for i in range(n + 1)}
        
        for edge in edges:
            matrix[edge[0]].append((edge[1], edge[2]))
            matrix[edge[1]].append((edge[0], edge[2]))
        

        parent = [i for i in range(n + 1)]
        distance = [float('inf')] * (n + 1)
        distance[1] = 0
        
        
        heap = [(0, 1)]
        
        while heap:
            curr_dist, node = heapq.heappop(heap)
            
            if curr_dist > distance[node]:
                continue
        
            for nei_node, dist in matrix[node]:
                new_dist = curr_dist + dist
                
                if new_dist < distance[nei_node]:
                    distance[nei_node] = new_dist
                    parent[nei_node] = node
                    heapq.heappush(heap, (new_dist, nei_node))
        

        if distance[n] == float('inf'):
            return [-1]

        path = []
        
        def find_path(target):
            if target == parent[target]:
                return
            else:
                find_path(parent[target])
            path.append(target)
        
        find_path(n)
        path.insert(0, 1)

        result = [distance[n]]
        result.extend(path)
        
        return result
        
        
        
