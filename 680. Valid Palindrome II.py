class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def validPalindromeHelper(s, left, right):
            while(left < right):
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                
                else:
                    return False
                
            return True

        left = 0
        right = len(s) - 1

        while (left < right):
            if s[left] == s[right]:
                left += 1
                right -= 1
            
            else:
                return validPalindromeHelper(s, left + 1, right) or validPalindromeHelper(s, left, right - 1)
            
        return True