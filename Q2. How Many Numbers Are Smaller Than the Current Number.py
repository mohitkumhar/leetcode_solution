class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        count = 0
        for i in nums:
            for num in nums:
                if i > num:
                    count += 1
            ans.append(count)
            count = 0

        return ans
