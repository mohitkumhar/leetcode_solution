class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        occurence = []

        for i in range(len(s)):
            if s[i] == c:
                occurence.append(i)

        answer = []
        for i in range(len(s)):
            if s[i] == c:
                answer.append(0)

            else:
                temp = []
                for j in range(len(occurence)):
                    temp.append(abs(occurence[j] - i))
                min_dist = min(temp)
                answer.append(min_dist)
        return answer
