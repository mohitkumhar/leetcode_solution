class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        def binary_search(end):
            nonlocal ans

            left = 0
            right = end

            while left <= right:
                mid = left + (right - left) // 2

                final_sum = nums[end] * (end - mid + 1)
                if mid == 0:
                    curr_sum = prefix_sum[end]
                else:
                    curr_sum = prefix_sum[end] - prefix_sum[mid - 1]

                total_opn = final_sum - curr_sum

                if total_opn <= k:
                    ans = max(ans, end - mid + 1)
                    right = mid - 1
                else:
                    left = mid + 1

        nums.sort()

        prefix_sum = [0] * len(nums)

        prefix_sum[0] = nums[0]

        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        ans = 0

        for i in range(len(nums)):
            binary_search(i)

        return ans
