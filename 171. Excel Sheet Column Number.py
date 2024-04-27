class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """

        initial_count = 0

        for char  in columnTitle:
            value = ord(char) - ord('A') + 1

            initial_count = initial_count * 26 + value

        return initial_count
        