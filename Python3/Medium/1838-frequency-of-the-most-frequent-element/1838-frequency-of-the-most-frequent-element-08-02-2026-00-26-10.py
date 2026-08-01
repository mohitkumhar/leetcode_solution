class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        n = len(nums)
        nums.sort()

        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]

        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        def binary_search(target_idx):
            nonlocal ans

            left = 0
            right = target_idx

            while left <= right:
                mid = left + (right - left) // 2

                final_sum = nums[target_idx] * (target_idx - mid + 1)
                if mid == 0:
                    curr_sum = prefix_sum[target_idx]
                else:
                    curr_sum = prefix_sum[target_idx] - prefix_sum[mid - 1]

                total_operations = final_sum - curr_sum

                if total_operations <= k:
                    ans = max(ans, target_idx - mid + 1)
                    right = mid - 1
                else:
                    left = mid + 1

        ans = 1
        for i in range(n):
            binary_search(i)

        return ans
