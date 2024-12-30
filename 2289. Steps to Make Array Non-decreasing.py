class Solution:
    def totalSteps(self, nums: List[int]) -> int:

        max_steps = 0
        stack = []

        for num in nums:
            steps = 0
            while stack and stack[-1][0] <= num:
                steps = max(steps, stack.pop()[1])


            stack.append((num, 0 if not stack else steps + 1))

            max_steps = max(max_steps, stack[-1][1])

        return max_steps