class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        left = 0
        right = n - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[right] > nums[mid]:
                right = mid
            else:
                left = mid + 1

        return nums[left]
