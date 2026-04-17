class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        ans = set()

        while left < right:
            small = nums[left]
            large = nums[right]

            ans.add((small+large)/2)

            left += 1
            right -= 1

        return len(ans)
