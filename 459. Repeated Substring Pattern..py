class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length_s = len(s)
        
        rpt = ''
        
        for i in range(length_s // 2):
            rpt += s[i]

            if length_s % len(rpt) == 0:

                if rpt * (length_s // len(rpt)) == s:
                    return True
            
        return False
                