class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:

        res = []

        for i in range(0, len(nums)-1, 2):
            temp = []

            temp.extend([nums[i + 1]] * nums[i])
            temp = [i for i in temp]
            res.extend(temp)

        return res