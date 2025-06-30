class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = k
        for num in nums:
            if num == 1:
                if count < k:
                    return False
                count = 0
            else:
                count += 1

        return True
