class Solution:
    def missingInteger(self, nums):
        sequentialSum = nums[0]
        n = len(nums)
        freq = [False] * 1276
        freq[nums[0]] = True

        i = 1
        while i < n:
            if nums[i] == nums[i - 1] + 1:
                sequentialSum += nums[i]
                freq[nums[i]] = True
            else:
                while i < n:
                    freq[nums[i]] = True
                    i += 1
                break
            i += 1

        for i in range(sequentialSum, 1277):
            if not freq[i]:
                return i
        return sequentialSum