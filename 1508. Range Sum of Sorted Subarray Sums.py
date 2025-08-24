class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        result = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                temp = sum(nums[i:j+1])
                result.append(temp)
        result.sort()

        return sum(result[left-1:right]) % MOD