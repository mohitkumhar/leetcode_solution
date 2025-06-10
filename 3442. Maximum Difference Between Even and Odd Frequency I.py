class Solution:
    def maxDifference(self, s: str) -> int:
        count = {
            'even': float('inf'),
            'odd': 0
        }

        for char in set(s):
            word_len = s.count(char)

            if word_len % 2 == 0:
                count['even'] = min(count['even'], word_len)
            else:
                count['odd'] = max(count['odd'], word_len)

        return count['odd'] - count['even']