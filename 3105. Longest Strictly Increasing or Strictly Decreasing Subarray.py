class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        inc_temp = 0
        dec_temp = 0

        inc_count = 0
        dec_count = 0

        prev = None

        for num in nums:
            if not prev:
                prev = num
                continue
            
            if num > prev:
                inc_temp += 1
            
            else:
                inc_temp = 0

            if num < prev:
                dec_temp += 1
            
            else:
                dec_temp = 0

            dec_count = max(dec_count, dec_temp)
            inc_count = max(inc_count, inc_temp)

            prev = num

        ans = max(dec_count, inc_count)

        return 1 if ans is 0 else ans + 1