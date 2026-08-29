class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:
        ans = 0
        n = len(nums)

        for remove in range(-1, n):
            arr = []

            for i in range(n):
                if i != remove:
                    arr.append(nums[i])

            m = len(arr)

            prefix = [0] * m
            prefix[0] = arr[0]

            for i in range(1, m):
                prefix[i] = gcd(prefix[i - 1], arr[i])

            suffix = [0] * m
            suffix[-1] = arr[-1]

            for i in range(m - 2, -1, -1):
                suffix[i] = gcd(suffix[i + 1], arr[i])

            count = 0

            for i in range(m - 1):
                if prefix[i] == suffix[i + 1]:
                    count += 1

            ans = max(ans, count)

        return ans
