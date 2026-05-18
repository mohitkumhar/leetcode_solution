class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)

        def solve(i, p1, p2):
            if i == n:
                return p1 == target and p2 == target

            if i >= n:
                return False

            take1 = False
            if p1 * nums[i] <= target:
                take1 = solve(i + 1, p1 * nums[i], p2)

            take2 = False
            if p2 * nums[i] <= target:
                take2 = solve(i + 1, p1, p2 * nums[i])


            return take1 or take2
        
        return solve(0, 1, 1)
        
