class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def partition(low, high):
            pivot = nums[low]
            pivot_index = low

            while low <= high:

                if nums[low] < pivot and nums[high] > pivot:
                    nums[low], nums[high] = nums[high], nums[low]
                    low += 1
                    high -= 1
                if low <= high and nums[low] >= pivot:
                    low += 1
                if low <= high and nums[high] <= pivot:
                    high -= 1
            nums[high], nums[pivot_index] = nums[pivot_index], nums[high]

            return high

        low = 0
        high = len(nums) - 1
        while True:
            pivot = partition(low, high)

            if pivot == k - 1:
                return nums[pivot]

            elif pivot < k - 1:
                low = pivot + 1

            else:
                high = pivot - 1

        return -1
