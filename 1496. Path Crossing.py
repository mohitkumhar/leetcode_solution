class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visit = set()
        pos = (0, 0)
        visit.add(pos)

        for char in path:
            x, y = pos

            if char == 'N':
                y += 1            
            elif char == 'S':
                y -= 1
            elif char == 'E':
                x += 1
            elif char == 'W':
                x -=1 

            pos = (x, y)

            if pos in visit:
                return True

            visit.add(pos)
        return False
