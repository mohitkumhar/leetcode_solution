class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        n = len(nums)

        left = 0
        right = n - 1

        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] == target:
                return True

            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1

            # left half is sorted
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False

