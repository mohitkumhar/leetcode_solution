class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = []
        sum = 0

        for i in s:
            record.append(ord(i))

        for i in range(1, len(record)):
            sum = sum + abs(record[i-1] - record[i])

        return sum
