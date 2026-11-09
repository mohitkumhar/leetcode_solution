class Solution:
    def mostCompetitive(self, nums: list[int], k: int) -> list[int]:

        stack = []
        n = len(nums)

        for i, num in enumerate(nums):
            while stack and stack[-1] > num and len(stack) + n - i > k:
                stack.pop()

            stack.append(num)

        return stack[:k]
