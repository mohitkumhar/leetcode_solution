class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        mn = 10**7
        ans = [area, 1]

        for width in range(1, (area // 2) + 1):
            if area % width == 0:
                length = area // width
                if length >= width and length - width < mn:
                    ans[0] = length
                    ans[1] = width
                    mn = length - width

        return ans
