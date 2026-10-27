class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        counter = {}

        for i in range(len(nums)):
            counter[nums[i]] = i

        for i in range(n):
            value = target - nums[i]
            if value in counter and counter[value] != i:
                return [i, counter[value]]
        return []
