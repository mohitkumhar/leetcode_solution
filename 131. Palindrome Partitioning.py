class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []

        def is_palindrome(arr):
            return arr == arr[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path)
                return 
        
            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start: end]):
                    backtrack(end, path + [s[start : end]])
        backtrack(0, [])

        return result