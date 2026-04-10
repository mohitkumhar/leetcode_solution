class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = float('inf')
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] == nums[j] == nums[k]:
                        ans = min(ans, abs(i - j) + abs(j - k) + abs(k - i))

        return ans if ans != float('inf') else -1
