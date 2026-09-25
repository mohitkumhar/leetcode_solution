class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def solve(k):
            seen = {}
            n = len(nums)

            i = 0
            j = 0
            count = 0

            while j < n:
                seen[nums[j]] = seen.get(nums[j], 0) + 1

                while len(seen) > k:
                    seen[nums[i]] -= 1
                    if seen[nums[i]] == 0:
                        del seen[nums[i]]
                    i += 1

                count += j - i + 1
                j += 1

            return count

        return solve(k) - solve(k - 1)
