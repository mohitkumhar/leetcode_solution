class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        zero_pairs = []
        count = 0
        for char in s:
            if char == "1":
                if count > 0:
                    zero_pairs.append(count)
                count = 0
            else:
                count += 1
        if count > 0:
            zero_pairs.append(count)

        maxi_ones = 0
        for i in range(len(zero_pairs) - 1):
            if (zero_pairs[i] + zero_pairs[i + 1]) > maxi_ones:
                maxi_ones = zero_pairs[i] + zero_pairs[i + 1]

        curr_ones = 0
        for char in s:
            if char == "1":
                curr_ones += 1

        return maxi_ones + curr_ones
