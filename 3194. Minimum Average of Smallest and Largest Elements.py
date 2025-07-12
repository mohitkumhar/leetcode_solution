class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        nums.sort()
        n = len(nums) // 2

        while n > 0:
            maxElement = nums.pop()
            minElement = nums.pop(0)
            averages.append((minElement + maxElement) / 2)
            n -= 1

        return min(averages)