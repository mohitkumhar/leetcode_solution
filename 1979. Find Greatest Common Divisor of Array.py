class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        mn = nums[0]
        mx = nums[-1]

        for i in range(mx, 0, -1):
            if mx % i == 0 and mn % i == 0:
                return i
