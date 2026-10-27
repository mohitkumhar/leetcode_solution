class Solution:
    def maxArea(self, heights: list[int]) -> int:
        n = len(heights)

        left = 0
        right = n - 1
        ans = 0

        while left < right:
            distance = right - left
            minHeight = min(heights[right], heights[left])
            ans = max(ans, distance * minHeight)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return ans
