class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        if nums[0] != 0:
            return 0

        for i in range(1, n):
            if (nums[i] - nums[i - 1]) > 1:
                return i

        return n
