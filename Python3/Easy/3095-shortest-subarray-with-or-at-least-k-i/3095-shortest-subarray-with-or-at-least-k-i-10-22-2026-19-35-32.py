class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = float("inf")

        for i in range(n):
            currOR = 0

            for j in range(i, n):
                currOR |= nums[j]

                if currOR >= k:
                    ans = min(ans, j - i + 1)
                    break

        return ans if ans != float("inf") else -1
