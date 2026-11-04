class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:

        n = len(rooms)

        queue = deque()
        queue.append(0)

        visited = set()
        visited.add(0)

        while queue:
            room = queue.popleft()

            for neiRooms in rooms[room]:
                if neiRooms not in visited:
                    visited.add(neiRooms)
                    queue.append(neiRooms)

        return len(visited) == n
