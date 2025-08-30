class Solution:
    def similarPairs(self, words: List[str]) -> int:
        def check(string1, string2):
            if all(s in string2 for s in string1):
                if all(s in string1 for s in string2):
                    return True
            return False
        ans = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if check(words[i], words[j]):
                    ans += 1
        return ans