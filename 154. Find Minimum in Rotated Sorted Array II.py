class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:

            while low < high and nums[low] == nums[low + 1]:
                low += 1
            while low < high and nums[high] == nums[high - 1]:
                high -= 1

            mid = low + (high - low) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return nums[low]
