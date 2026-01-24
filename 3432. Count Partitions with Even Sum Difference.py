class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count = 0

        for i in range(1, len(nums)):
            left_sum = nums[:i]
            right_sum = nums[i:]

            if abs(sum(left_sum) - sum(right_sum)) % 2 == 0:
                count += 1

        return count
