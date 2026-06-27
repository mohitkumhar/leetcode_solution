from collections import Counter
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 1

        # Handle 1 separately
        if 1 in freq:
            ans = freq[1]
            if ans % 2 == 0:
                ans -= 1

        def solve(x):
            if freq[x] == 0:
                return 0

            # Can't use two copies
            if freq[x] == 1:
                return 1

            # Use two copies and continue
            nxt = solve(x * x)

            if nxt == 0:
                return 1
            return 2 + nxt

        for x in freq:
            if x == 1:
                continue
            ans = max(ans, solve(x))

        return ans