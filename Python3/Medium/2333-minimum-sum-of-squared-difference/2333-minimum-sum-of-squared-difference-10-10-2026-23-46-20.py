class Solution:
    def minSumSquareDiff(
        self, nums1: list[int], nums2: list[int], k1: int, k2: int
    ) -> int:
        n = len(nums1)

        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        maxDiff = max(diff)

        countDiff = [0] * (maxDiff + 1)

        for d in diff:
            countDiff[d] += 1

        K = k1 + k2

        for currDiff in range(maxDiff, 0, -1):
            if K == 0:
                break

            countOps = min(countDiff[currDiff], K)

            countDiff[currDiff] -= countOps
            countDiff[currDiff - 1] += countOps
            K -= countOps

        result = 0

        for d in range(1, maxDiff + 1):
            result += countDiff[d] * d * d

        return result