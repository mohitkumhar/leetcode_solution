class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = [0]

        while queue:
            value = queue.pop(0)
            if value in visited:
                continue

            visited.add(value)
            next_key = rooms[value]

            for key in next_key:
                queue.append(key)

        return len(visited) == len(rooms)
