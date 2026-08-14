class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        left = 1
        right = n - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] == nums[mid + 1]:
                if (right - mid) % 2 == 0:
                    left = mid + 2
                else:
                    right = mid - 1

            else:
                if (right - mid) % 2 == 0:
                    right = mid

                else:
                    left = mid + 1

        return nums[right]
