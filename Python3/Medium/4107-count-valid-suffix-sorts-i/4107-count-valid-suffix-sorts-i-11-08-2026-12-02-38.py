class Solution:
    def countSuffix(self, nums: list[int], target: list[int]) -> int:
        n = len(nums)

        freq = [0] * 100001

        for x in nums:
            freq[x] += 1
        for x in target:
            freq[x] -= 1

        result = 0
        prefix = True
        nonzero = sum(x != 0 for x in freq)

        sorted_suffix = [True] * n

        for i in range(n - 2, -1, -1):
            sorted_suffix[i] = sorted_suffix[i + 1] and target[i] >= target[i + 1]

        for i in range(n):
            if prefix and sorted_suffix[i] and nonzero == 0:
                result += 1

            x = nums[i]
            if freq[x] == 0:
                nonzero += 1
            freq[x] -= 1
            if freq[x] == 0:
                nonzero -= 1

            x = target[i]
            if freq[x] == 0:
                nonzero += 1
            freq[x] += 1
            if freq[x] == 0:
                nonzero -= 1

            if nums[i] != target[i]:
                prefix = False

        return result
