class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = -1  # all bits set: nothing misplaced yet
        for i, x in enumerate(nums):
            if x != i:  # this number has to move
                k &= x  # keep only the bits it shares
                if not k:  # bits only disappear, so 0 stays 0
                    return 0
        return max(k, 0)  # -1 means nothing has to move