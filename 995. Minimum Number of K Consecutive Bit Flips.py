class Solution(object):
    def minKBitFlips(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        n = len(nums)
        flips = 0
        isFlipped = [False] * n
        pastFlipCount = 0

        for i in range(n):
            if i and isFlipped[i-k] == True:
                pastFlipCount -= 1

            if (pastFlipCount % 2 == 0 and nums[i] == 0) or (pastFlipCount % 2 != 0 and nums[i] == 1):
                if i + k > n:
                    return -1

                flips += 1
                pastFlipCount += 1
                isFlipped[i] = True
        return flips
