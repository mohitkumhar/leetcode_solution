class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        def checkFreq(s):
            freq = {}
            for char in s:
                if char in freq:
                    return True
                freq[char] = 1
            return False

        if len(s) != len(goal):
            return False

        if s == goal:
            return checkFreq(s)

        index = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                index.append(i)

        if len(index) != 2:
            return False

        i, j = index
        s_list = list(s)

        s_list[i], s_list[j] = s_list[j], s_list[i]

        return ''.join(s_list) == goal
