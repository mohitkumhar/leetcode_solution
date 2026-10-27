class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        n = len(nums)
        ans = 1
        count = 1

        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                continue

            if nums[i] + 1 == nums[i + 1]:
                count += 1
            else:
                count = 1

            ans = max(ans, count)

        return ans
