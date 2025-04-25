class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """        
        result = []

        def backtrack(start, current):
            if len(current) == k and sum(current) == n:
                result.append(current[:])
            if len(current) > k or sum(current) > n:
                return

            for i in range(start, 10):
                backtrack(i + 1, current + [i])
        backtrack(1, [])

        return result
