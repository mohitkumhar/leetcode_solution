class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        answer = 0
        for i in range(0, len(s)-k+1):
            temp = 0
            sub_str = s[i:i+k]
            temp += sub_str.count('a')
            temp += sub_str.count('e')
            temp += sub_str.count('i')
            temp += sub_str.count('o')
            temp += sub_str.count('u')

            answer = max(temp, answer)
        return answer
