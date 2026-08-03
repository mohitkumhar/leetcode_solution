class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        currSum = 0
        prefixSum = {0: 1}

        for i in range(len(nums)):
            currSum += nums[i]

            if (currSum - k) in prefixSum:
                count += prefixSum[currSum - k]

            prefixSum[currSum] = prefixSum.get(currSum, 0) + 1

        return count
