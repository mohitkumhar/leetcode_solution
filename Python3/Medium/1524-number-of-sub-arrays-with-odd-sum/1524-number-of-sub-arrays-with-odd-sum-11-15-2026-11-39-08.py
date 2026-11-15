class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        prefixSum = 0
        MOD = 10**9 + 7
        evenCount = 1
        oddCount = 0

        for num in arr:
            prefixSum += num

            if prefixSum % 2 == 1:
                oddCount += 1
            else:
                evenCount += 1

        return (oddCount * evenCount) % MOD
