class Solution:
    def maxSumTwoNoOverlap(self, nums: list[int], firstLen: int, secondLen: int) -> int:

        def helper(l, r):
            n = len(prefixSum)
            maxLeftSubSum = 0
            result = 0

            for rEnd in range(l + r - 1, n):
                lEnd = rEnd - r
                lStart = lEnd - l

                lBlockSum = prefixSum[lEnd] - (prefixSum[lStart] if lStart >= 0 else 0)
                rBlockSum = prefixSum[rEnd] - prefixSum[lEnd]

                maxLeftSubSum = max(maxLeftSubSum, lBlockSum)

                result = max(result, maxLeftSubSum + rBlockSum)

            return result

        n = len(nums)

        prefixSum = [0] * n
        prefixSum[0] = nums[0]

        for i in range(1, n):
            prefixSum[i] = prefixSum[i - 1] + nums[i]

        return max(helper(firstLen, secondLen), helper(secondLen, firstLen))
