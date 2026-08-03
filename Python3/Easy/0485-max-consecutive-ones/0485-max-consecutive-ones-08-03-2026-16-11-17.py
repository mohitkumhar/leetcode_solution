class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxOnes = 0
        for num in nums:
            if num == 1:
                count += 1
                maxOnes = max(maxOnes, count)
            else:
                count = 0
        return maxOnes
