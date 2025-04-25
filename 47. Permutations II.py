class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        n = len(nums)
        used = [False] * n

        def backtrack(current):
            if len(current) == n:
                result.append(current[:])
                return
            
            for i in range(n):
                if used[i]:
                    continue
                
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                used[i] = True
                current.append(nums[i])
                backtrack(current)
                current.pop()
                used[i] = False

        backtrack([])

        return result
