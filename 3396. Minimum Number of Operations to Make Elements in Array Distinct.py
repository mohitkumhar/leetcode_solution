class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def check_distinct(arr):
            seen = set()
            for char in arr:
                if char in seen:
                    return True
                seen.add(char)
            return False

        ans = 0
        i = 0
        while len(nums) >= 3 and check_distinct(nums):
            ans += 1
            nums = nums[3:]
            i += 1
        
        if check_distinct(nums):
            ans += 1
        return ans
