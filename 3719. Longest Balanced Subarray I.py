class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            seen = set()
            j = i
            odd = 0
            even = 0

            while j < n:
                if nums[j] not in seen:
                    seen.add(nums[j])
                    if nums[j] % 2 == 0:
                        even += 1
                    else:
                        odd += 1

                if odd == even:
                    ans = max(ans, j - i + 1)
                j += 1

        return ans
