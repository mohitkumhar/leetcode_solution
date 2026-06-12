class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cum_sum = [0] * n
        j = 0
        min_arr = float('inf')
        deque = []

        while j < n:
            if j == 0:
                cum_sum[j] = nums[j]
            else:
                cum_sum[j] = cum_sum[j - 1] + nums[j]

            if cum_sum[j] >= k:
                min_arr = min(min_arr, j + 1)

            while deque and cum_sum[j] - cum_sum[deque[0]] >= k:
                min_arr = min(min_arr, j - deque[0])
                deque.pop(0)

            while deque and cum_sum[j] < cum_sum[deque[-1]]:
                deque.pop()

            deque.append(j)
            j += 1

        return -1 if min_arr == float('inf') else min_arr
