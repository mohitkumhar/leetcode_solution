class Solution(object):
    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """

        ans = [str(words[0])]
        n = len(words)

        for i in range(1, n):
            if groups[i] != groups[i - 1]:
                ans.append(words[i])
        return ans
