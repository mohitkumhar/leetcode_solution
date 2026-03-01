class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        found = False
        for char in s:
            if char == "a":
                if found:
                    return False
            else:
                found = True
        return True
