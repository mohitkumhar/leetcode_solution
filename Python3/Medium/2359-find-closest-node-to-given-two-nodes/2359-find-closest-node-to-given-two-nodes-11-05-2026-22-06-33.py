class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        n = len(edges)

        def find_dist(node):
            distance = [float("inf") for i in range(n)]
            queue = deque([(node, 0)])
            visited = set()

            while queue:
                node, dist = queue.popleft()
                if node in visited:
                    continue
                visited.add(node)
                distance[node] = dist

                if edges[node] != -1 and edges[node] not in visited:
                    queue.append((edges[node], dist + 1))

            return distance

        dist1 = find_dist(node1)
        dist2 = find_dist(node2)

        distance = []

        ans = -1
        best = float("inf")

        for i in range(n):
            if dist1[i] == float("inf") or dist2[i] == float("inf"):
                continue

            currDist = max(dist1[i], dist2[i])

            if currDist < best:
                best = currDist
                ans = i

        return ans
