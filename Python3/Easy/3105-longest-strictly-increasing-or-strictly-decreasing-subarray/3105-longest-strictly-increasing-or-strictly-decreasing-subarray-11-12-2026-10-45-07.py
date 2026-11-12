class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1

        currIncCount = 0
        currDecCount = 0

        incCount = 0
        decCount = 0

        prev = None

        for num in nums:
            if prev is None:
                prev = num
                continue

            if num > prev:
                currIncCount += 1
            else:
                currIncCount = 0

            if num < prev:
                currDecCount += 1
            else:
                currDecCount = 0
            
            incCount = max(incCount, currIncCount)
            decCount = max(decCount, currDecCount)

            prev = num

        ans = max(incCount, decCount)

        return 1 if ans == 0 else ans + 1
