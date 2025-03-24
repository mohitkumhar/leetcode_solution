class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        stack = []
        ans = 0

        for num in nums:
            if len(stack) % 2 == 0 or stack[-1] != num:
                stack.append(num)
            else:
                ans += 1
                
        if len(stack) % 2 == 1:
            ans += 1
        
        return ans