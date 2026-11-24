class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def first():
            left = 0
            right = n - 1
            ans = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    ans = mid
                    right = mid - 1

                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        def second():
            left = 0
            right = n - 1
            ans = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    ans = mid
                    left = mid + 1

                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        n = len(nums)
        return [first(), second()]
