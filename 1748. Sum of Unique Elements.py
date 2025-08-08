class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        ans = 0
        for key, value in count.items():
            if value == 1:
                ans += key
        return ans
