class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        left = 1
        right = n - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] == nums[mid + 1]:
                if (right - mid) % 2 == 1:  # if elements are odd from the curr idx
                    right = mid - 1
                else:
                    left = mid + 2

            else:
                if (right - mid) % 2 == 1:  # if elements are odd from the curr idx
                    left = mid + 1
                else:
                    right = mid

        return nums[right]
