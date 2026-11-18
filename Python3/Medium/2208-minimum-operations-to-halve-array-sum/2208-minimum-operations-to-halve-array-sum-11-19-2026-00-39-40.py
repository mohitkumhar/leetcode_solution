class Solution:
    def halveArray(self, nums: list[int]) -> int:
        currSum = sum(nums)
        targetSum = currSum / 2
        count = 0

        nums = [-num for num in nums]
        heapq.heapify(nums)

        while currSum > targetSum:

            highValue = -heapq.heappop(nums)
            newVal = highValue / 2

            heapq.heappush(nums, -newVal)
            currSum -= newVal

            count += 1

        return count
