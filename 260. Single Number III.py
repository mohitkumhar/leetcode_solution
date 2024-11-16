class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        count = {}

        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        ans = [ind for ind, value in count.items() if value == 1]

        return ans
