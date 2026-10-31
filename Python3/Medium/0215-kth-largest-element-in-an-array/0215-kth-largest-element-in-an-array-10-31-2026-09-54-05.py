class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:

        def findPivot(left, right):
            pivot = nums[left]
            pivotIdx = left

            while left <= right:

                if nums[left] < pivot and nums[right] > pivot:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1

                if left <= right and nums[left] >= pivot:
                    left += 1

                if left <= right and nums[right] <= pivot:
                    right -= 1

            nums[right], nums[pivotIdx] = nums[pivotIdx], nums[right]

            return right

        n = len(nums)

        left = 0
        right = n - 1

        while left <= right:
            pivot = findPivot(left, right)

            if pivot == k - 1:
                return nums[pivot]

            elif pivot > k - 1:
                right = pivot - 1
            else:
                left = pivot + 1

        return -1
