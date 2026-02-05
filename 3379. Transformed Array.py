class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        n = len(nums)

        for i in range(len(nums)):
            temp = (i + nums[i]) % n
            result[i] = nums[temp]

        return result
