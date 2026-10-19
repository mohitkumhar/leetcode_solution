class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)

        i = 0
        j = 0

        ans = []
        queue = []

        while j < n:
            while queue and nums[queue[-1]] < nums[j]:
                queue.pop()
            queue.append(j)

            if (j - i + 1) < k:
                j += 1

            elif (j - i + 1) == k:
                ans.append(nums[queue[0]])

                if nums[i] == nums[queue[0]]:
                    queue.pop(0)
                i += 1
                j += 1

        return ans
