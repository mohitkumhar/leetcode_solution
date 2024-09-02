class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        (x1, y1), (x2, y2), (x3, y3) = points

        if (x1, y1) == (x2, y2) or (x2, y2) == (x3, y3) or (x1, y1) == (x3, y3):
            return False
        

        area = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

        return area != 0
        