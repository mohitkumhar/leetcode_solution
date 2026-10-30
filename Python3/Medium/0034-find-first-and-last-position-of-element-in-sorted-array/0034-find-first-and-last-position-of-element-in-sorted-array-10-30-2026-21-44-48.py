class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)

        firstPos = -1
        secondPos = -1

        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                firstPos = mid
                secondPos = mid
                temp = mid
                while nums[temp] == target:
                    temp -= 1
                firstPos = temp + 1

                temp = mid
                while nums[temp] == target:
                    temp += 1
                secondPos = temp - 1
                return [firstPos, secondPos]

            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return [-1, -1]
