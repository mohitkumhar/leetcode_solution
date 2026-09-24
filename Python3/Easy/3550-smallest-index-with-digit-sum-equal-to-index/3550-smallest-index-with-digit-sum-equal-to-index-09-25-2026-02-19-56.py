class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sum_num(val):
            num = 0
            for v in val:
                num += int(v)
            return num

        for i, num in enumerate(nums):
            if sum_num(str(num)) == i:
                return i
        return -1
