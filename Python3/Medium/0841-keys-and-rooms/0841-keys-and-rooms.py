class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        matrix = {i: [] for i in range(n)}

        for i in range(n):
            matrix[i].extend(rooms[i])

        queue = deque([0])
        visited = set()

        while queue:
            idx = queue.popleft()
            if idx in visited:
                continue
            visited.add(idx)

            for other_rooms in matrix.get(idx, []):
                if other_rooms not in visited:
                    queue.append(other_rooms)

        return n == len(visited)
