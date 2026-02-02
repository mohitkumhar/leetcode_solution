class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        left = 0
        right = len(colors) - 1
        ans = 0

        while left < right:
            if colors[left] != colors[right]:
                ans = max(ans, abs(left - right))
            right -= 1

        right = len(colors) - 1
        while left < right:
            if colors[left] != colors[right]:
                ans = max(ans, abs(left - right))
            left += 1

        return ans
