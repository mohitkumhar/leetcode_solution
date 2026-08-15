class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        currXOR = 0

        for num in nums:
            currXOR ^= num

        numsSet = set(nums)

        if len(numsSet) == 1 and 0 in numsSet:
            return 0

        if currXOR != 0:
            return len(nums)
        return len(nums) - 1
