class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        result = 0

        prev = 0
        curr = 0

        for i in range(len(nums)):
            curr = target[i] - nums[i]

            if prev > 0 and curr < 0 or prev < 0 and curr > 0:
                result += abs(curr)

            elif abs(prev) < abs(curr):
                result += abs(prev - curr)

            prev = curr

        return result
