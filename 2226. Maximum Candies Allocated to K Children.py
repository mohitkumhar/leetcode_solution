class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        left = 1
        right = max(candies)
        best = 0

        while left <= right:
            mid = (left + right) // 2
            count = 0

            for candie in candies:
                count += candie // mid
            
            if count >= k:
                best = mid
                left = mid + 1
            
            else:
                right = mid - 1
        
        return best
