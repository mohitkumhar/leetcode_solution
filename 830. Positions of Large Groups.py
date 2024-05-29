class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        result = []
        n = len(s)
        i = 0

        while i < n:
            start = i

            while i < n and s[i] == s[start]:
                i += 1
                print(i)

            print('this is outside i', i)

            if i - start >= 3:
                result.append([start, i - 1])
                print('if', i)

        return result
