class Solution(object):
    def zigzagTraversal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        result = []
        for i in range(len(grid)):
            if i % 2 == 0:
                result.extend(grid[i])
            else:
                result.extend(grid[i][::-1])

        ans = []
        i = 0
        for res in result:
            if i % 2 == 0:
                ans.append(res)
            i += 1
        return ans
