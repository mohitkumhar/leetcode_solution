class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        i = 0
        j = len(s) - 1
        vowel = set('aeiou')

        while i < j:

            if s_list[i].lower() in vowel and s_list[j].lower() in vowel:
                temp = s_list[i]
                s_list[i] = s_list[j]
                s_list[j] = temp
                i += 1
                j -= 1

            if s_list[i].lower() not in vowel:
                i += 1

            if s_list[j].lower() not in vowel:
                j -= 1

        return ''.join(s_list)
