class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixTable = {0: 1}
        count = 0
        prefixSum = 0

        for i in range(len(nums)):

            prefixSum += nums[i]

            if (prefixSum - k) in prefixTable:
                count += prefixTable[prefixSum - k]

            prefixTable[prefixSum] = prefixTable.get(prefixSum, 0) + 1

        return count
