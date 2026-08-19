class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        operations = 0

        for i in range(n - 2, -1, -1):

            parts = nums[i] // nums[i + 1]

            if nums[i] % nums[i + 1] != 0:
                parts += 1

            operations += parts - 1

            nums[i] = nums[i] // parts

        return operations
