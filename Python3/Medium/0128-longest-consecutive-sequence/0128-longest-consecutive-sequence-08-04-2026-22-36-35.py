class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        n = len(nums)
        currSeq = 1
        maxSeq = 1

        for i in range(1, n):
            if (nums[i]) == nums[i - 1]:
                continue
            elif (nums[i] - 1) == nums[i - 1]:
                currSeq += 1
            elif (nums[i] - 1) != nums[i - 1]:
                currSeq = 1

            maxSeq = max(maxSeq, currSeq)

        return maxSeq
