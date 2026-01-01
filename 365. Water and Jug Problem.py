class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        jugx = x
        jugy = y
        x=0
        y=0

        queue = [(0, 0)]
        visited = set()

        while queue:
            x, y = queue.pop(0)

            if (x, y) in visited:
                continue
            visited.add((x, y))

            if x == target or y == target or x + y == target:
                return True

            next_state = []
            
            # Fill either jug completely with water
            # left jug
            next_state.append((jugx, y))
            # right jug
            next_state.append((x, jugy))


            # Completely empty either jug.
            # left jug
            next_state.append((0, y))
            # right jug
            next_state.append((x, 0))
        

            # Pour water from one jug into another
            # jug1 -> jug2
            water = min(x, jugy - y)
            next_state.append((x - water, y + water))

            # jug2 -> jug1
            water = min(jugx - x, y)
            next_state.append((x + water, y - water))

            for state in next_state:
                if not state in visited:
                    queue.append(state)

        return False
