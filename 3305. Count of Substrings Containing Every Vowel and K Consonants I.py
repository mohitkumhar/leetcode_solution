class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        ans = 0

        for i in range(n):
            vowels = set()
            consonants = 0
            for j in range(i, n):
                if word[j] in "aeiou":
                    vowels.add(word[j])
                else:
                    consonants += 1

                if consonants > k:
                    break

                if consonants == k and len(vowels) == 5:
                    ans += 1
        return ans
