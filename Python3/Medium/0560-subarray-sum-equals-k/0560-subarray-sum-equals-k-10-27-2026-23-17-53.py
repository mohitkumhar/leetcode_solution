class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        count = 0
        prefixCount = {0: 1}

        for num in nums:
            prefixSum += num

            count += prefixCount.get(prefixSum - k, 0)

            prefixCount[prefixSum] = prefixCount.get(prefixSum, 0) + 1

        return count
