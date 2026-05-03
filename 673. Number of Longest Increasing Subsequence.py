class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sequence = [1 for _ in range(n)]
        count = [1 for _ in range(n)]

        for i in range(n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    if sequence[j] + 1 > sequence[i]:
                        sequence[i] = sequence[j] + 1
                        count[i] = count[j]

                    elif sequence[j] + 1 == sequence[i]:
                        count[i] += count[j]

        max_len = max(sequence)
        result = 0
        for i in range(n):
            if sequence[i] == max_len:
                result += count[i]
        return result
