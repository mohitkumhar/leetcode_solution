class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        contains1 = False
        if 1 in nums:
            contains1 = True

        if contains1 == False:
            return 1

        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = 1

        for i in range(n):
            num = abs(nums[i])

            if (num - 1) < n:
                nums[num - 1] = -abs(nums[num - 1])

        for i in range(n):
            if nums[i] < 0:
                continue

            return i + 1

        return n + 1
