class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        x_to_z = abs(x - z)
        y_to_z = abs(y - z)
        if x_to_z < y_to_z:
            return 1
        elif y_to_z < x_to_z:
            return 2
        else:
            return 0
