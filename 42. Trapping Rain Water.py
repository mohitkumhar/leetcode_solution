class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)

        prev_greatest_element = []
        greatest_element = 0 

        for i in range(n):
            prev_greatest_element.append(greatest_element)
            greatest_element = max(greatest_element, height[i])

        next_greatest_element = []
        greatest_element = 0 

        for i in range(n-1, -1, -1):
            next_greatest_element.append(greatest_element)
            greatest_element = max(greatest_element, height[i])
        next_greatest_element = next_greatest_element[::-1]

        ans = 0
        for i in range(n):
            ans += max(0, min(next_greatest_element[i], prev_greatest_element[i]) - height[i])

        return ans
