class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] =1

        for value in count.values():
            if value > 2:
                return False
        return True
