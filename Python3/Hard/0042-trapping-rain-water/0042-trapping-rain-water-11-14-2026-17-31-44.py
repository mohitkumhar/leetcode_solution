class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)

        leftSideGreatestElement = []
        stack = []

        for i in range(n):

            if not stack:
                leftSideGreatestElement.append(-1)
            else:
                leftSideGreatestElement.append(stack[-1])

            if not stack or height[i] > stack[-1]:
                stack.append(height[i])

        rightSideGreatestElement = []
        stack = []

        for i in range(n - 1, -1, -1):
            if not stack:
                rightSideGreatestElement.append(-1)
            else:
                rightSideGreatestElement.append(stack[-1])

            if not stack or height[i] > stack[-1]:
                stack.append(height[i])

        rightSideGreatestElement = rightSideGreatestElement[::-1]

        ans = 0

        for i in range(n):  # O(n)
            currWaterLevel = min(
                leftSideGreatestElement[i], rightSideGreatestElement[i]
            )

            ans += max(0, currWaterLevel - height[i])

        return ans
