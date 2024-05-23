class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def area(p1, p2, p3):
            return abs(p1[0] * (float(p2[1]) - float(p3[1])) + p2[0] * (float(p3[1]) - float(p1[1])) + p3[0] * (float(p1[1]) - float(p2[1]))) / 2

        n = len(points)
        max_area = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    max_area = max(
                        area(points[i], points[j], points[k]), max_area)

        return max_area
