class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def find_pivot():
            left = 0
            right = n - 1

            while left < right:
                mid = left + (right - left) // 2

                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid

            return right

        def binary_search(left, right):
            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    return mid

                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid-1

            return -1

        pivot = find_pivot()

        left_idx = binary_search(0, pivot - 1)
        right_idx = binary_search(pivot, n-1)

        return max(left_idx, right_idx)
