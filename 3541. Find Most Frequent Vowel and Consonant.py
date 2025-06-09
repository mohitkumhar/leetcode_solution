class Solution:
    def maxFreqSum(self, s: str) -> int:
        vov = 0
        cons = 0

        vowel = set('aeiou')
        count = {}

        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        for key, value in count.items():
            if key in vowel:
                vov = max(vov, value)
            else:
                cons = max(cons, value)

        return cons + vov
