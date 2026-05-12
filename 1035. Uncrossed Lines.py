class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m = len(nums1)
        n = len(nums2)
        memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]

        def solve(i, j):
            if i >= m or j >= n:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]

            take = 0
            if nums1[i] == nums2[j]:
                take = 1 + solve(i + 1, j + 1)

            skip_left = solve(i + 1, j)
            skip_right = solve(i, j + 1)

            memo[i][j] = max(take, skip_left, skip_right)

            return max(take, skip_left, skip_right)

        return solve(0, 0)
