class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        elements = set(nums)
        maxSeq = 1

        for num in elements:
            currSeq = 0
            if (num - 1) in elements:
                continue

            else:
                i = 1
                while (num + 1) in elements:
                    i += 1
                    num += 1

                currSeq = i

                maxSeq = max(maxSeq, currSeq)

        return maxSeq
