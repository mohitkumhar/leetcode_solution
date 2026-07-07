class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        matrix = {i:[] for i in range(n)}

        for u, v, w in edges:
            if online[u] and online[v]:
                matrix[u].append((v, w))

        def check(mid):
            distance = [float('inf')] * n
            distance[0] = 0

            heap = [(0, 0)]

            while heap:
                curr_dist, node = heapq.heappop(heap)

                if curr_dist > k:
                    return False
                if node == (n-1):
                    return True
                if curr_dist > distance[node]:
                    continue

                for v, w in matrix.get(node, []):
                    if w < mid:
                        continue

                    new_dist = curr_dist + w
                    if new_dist < distance[v]:
                        distance[v] = new_dist
                        heapq.heappush(heap, (new_dist, v))

            return False

        left = 0
        right = 10**9
        ans = -1

        while left <= right:
            mid = (right + left) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
