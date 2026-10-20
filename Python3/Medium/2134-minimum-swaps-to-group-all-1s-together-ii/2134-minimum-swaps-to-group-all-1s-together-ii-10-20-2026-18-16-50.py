class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        k = nums.count(1)
        if k == 0 or k == len(nums):
            return 0

        nums = nums + nums

        i = 0
        j = 0
        n = len(nums)

        ans = float("inf")
        currOne = 0

        while j < n:
            if nums[j] == 1:
                currOne += 1

            if j - i + 1 == k:
                ans = min(ans, k - currOne)

                if nums[i] == 1:
                    currOne -= 1
                i += 1

            j += 1

        return ans
