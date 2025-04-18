class Solution(object):
    def validStrings(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        def backtrack(current):
            if len(current) == n:
                result.append(current)
                return
            
            backtrack(current + '1')
            if len(current) == 0 or current[-1] == '1':
                backtrack(current + '0')
        backtrack('')
        
        return result
