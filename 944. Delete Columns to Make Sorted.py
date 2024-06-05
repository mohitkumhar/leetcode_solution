class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """

        rows = len(strs)
        cols = len(strs[0])

        count = 0

        for j in range(cols):
            for i in range(1, rows):
                if strs[i][j] < strs[i - 1][j]:
                    count += 1
                    break
        return count
