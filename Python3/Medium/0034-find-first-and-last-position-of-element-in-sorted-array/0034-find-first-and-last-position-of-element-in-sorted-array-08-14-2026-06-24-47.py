class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                left = mid
                while left > 0 and nums[left - 1] == target:
                    left -= 1

                right = mid
                while right < n and nums[right + 1] == target:
                    right += 1

                return [left, right]

            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return [-1, -1]
