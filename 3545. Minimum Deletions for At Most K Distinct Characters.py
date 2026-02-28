class Solution(object):
    def minDeletion(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        counter = {}
        for char in s:
            if char not in counter:
                counter[char] = 0
            counter[char] += 1

        if len(counter) <= k:
            return 0

        # store the ascendeing order values
        freq = sorted(counter.values())
        deletion = 0
        how_much_delete = len(counter) - k

        for i in range(how_much_delete):
            deletion += freq[i]

        return deletion
