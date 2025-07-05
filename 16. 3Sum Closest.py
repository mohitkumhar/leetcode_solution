class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        min_diff = float('inf')

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                curr_diff = abs(current_sum - target)

                if curr_diff < min_diff:
                    min_diff = curr_diff
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest_sum