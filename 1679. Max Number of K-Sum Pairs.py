class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        count = 0
        left = 0
        right = n - 1

        while left < right:
            sum = nums[left] + nums[right]
            if sum == k:
                count += 1
                left += 1
                right -= 1

            else:
                if sum < k:
                    left += 1
                else:
                    right -= 1

        return count
