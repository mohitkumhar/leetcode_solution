class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        s = s.upper()
        s = s[::-1]
        s = s.replace("-", "")
        result = []

        for i in range(0, len(s), k):
            result.append(s[i:i+k])
        
        return "-".join(result)[::-1]


        