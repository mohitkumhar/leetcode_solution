class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        def can_rob(cap):
            count = 0 
            i = 0

            while i < len(nums) and count < k:
                if nums[i] <= cap:
                    count += 1
                    i += 2
                
                else:
                    i += 1
                
            return count >= k
        
        left = min(nums)
        right = max(nums)
    
        while left < right:
            mid = (left + right) // 2

            if can_rob(mid):
                right = mid
            
            else:
                left = mid + 1
        
        return left
