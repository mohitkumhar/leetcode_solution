class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        while sum(nums) % k != 0:
            max_ind = nums.index(max(nums))
            nums[max_ind] -= 1
            count += 1

        return count
