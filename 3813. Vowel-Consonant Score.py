class Solution(object):
    def vowelConsonantScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels = set('aeiou')
        vowel = 0
        const = 0

        for char in s:
            if char in vowels:
                vowel += 1
            elif char.isalpha():
                const += 1

        score = 0
        if const > 0:
            score = math.floor(vowel // const)

        return int(score)
