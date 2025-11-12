class Solution:
    def maxSum(self, nums: List[int]) -> int:
        def check_max(val):
            max_val = 0
            for char in val:
                max_val = max(max_val, int(char))
            return max_val

        nums.sort(reverse=True)
        max_sum = -1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if check_max(str(nums[i])) == check_max(str(nums[j])):
                    max_sum = max(max_sum, nums[i] + nums[j])
        return max_sum
