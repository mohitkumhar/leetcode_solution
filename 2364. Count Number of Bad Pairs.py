class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        freq = {}
        good_pair = 0
        n = len(nums)

        for i in range(n):
            diff = nums[i] - i

            if diff in freq:
                good_pair += freq[diff]
                freq[diff] += 1
            else:
                freq[diff] = 1

        total_pairs = n*(n - 1)// 2

        return total_pairs - good_pair
