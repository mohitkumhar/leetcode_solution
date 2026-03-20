class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        n = len(nums)
        maximum_elements = []
        ans = []

        for j in range(n):
            while maximum_elements and maximum_elements[-1] < nums[j]:
                maximum_elements.pop()

            maximum_elements.append(nums[j])
            mx = maximum_elements[0]

            if j - i + 1 == k:
                ans.append(mx)
                if nums[i] == mx:
                    maximum_elements.pop(0)

                i += 1

        return ans
