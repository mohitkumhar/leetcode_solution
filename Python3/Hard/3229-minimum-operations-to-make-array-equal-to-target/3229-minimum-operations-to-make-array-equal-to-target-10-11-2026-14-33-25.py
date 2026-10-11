class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:

        result = 0

        prev = 0
        curr = 0

        for i in range(len(nums)):
            curr = target[i] - nums[i]

            # check if number sign is changed
            if curr > 0 and prev < 0 or curr < 0 and prev > 0:
                result += abs(curr)

            elif abs(curr) > abs(prev):
                result += abs(prev - curr)

            prev = curr

        return result
