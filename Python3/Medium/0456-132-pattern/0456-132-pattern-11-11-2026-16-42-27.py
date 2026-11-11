class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        n = len(nums)
        stack = []
        num_3 = float("-inf")

        for i in range(n - 1, -1, -1):
            if nums[i] < num_3:
                return True

            while stack and nums[i] > stack[-1]:
                num_3 = stack.pop()

            stack.append(nums[i])

        return False
