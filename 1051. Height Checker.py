class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        expected = sorted(heights)
        i = 0
        count = 0

        while i != len(heights):
            if heights[i] != expected[i]:
                count += 1
            i += 1

        return count
