class Solution:
    def maxSubarraySum(self, arr):
        n = len(arr)
        curr_sum = arr[0]
        max_sum = arr[0]

        for i in range(1, n):
            curr_sum = max(arr[i], arr[i] + curr_sum)
            max_sum = max(max_sum, curr_sum)

        return max_sum
