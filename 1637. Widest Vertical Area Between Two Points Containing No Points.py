class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        array = []
        for point in points:
            array.append(point[0])

        array.sort()
        result = 0
        for i in range(len(array) - 1):
            result = max(result, array[i + 1] - array[i])
        return result
