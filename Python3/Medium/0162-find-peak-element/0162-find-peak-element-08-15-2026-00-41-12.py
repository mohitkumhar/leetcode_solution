class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        n = len(nums)

        if n <= 2:
            return max(nums)

        left = 0
        right = n - 1

        while left < right:

            mid = left + (right - left) // 2

            if mid > 0 and mid < (n - 1) and nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid

            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return -1
