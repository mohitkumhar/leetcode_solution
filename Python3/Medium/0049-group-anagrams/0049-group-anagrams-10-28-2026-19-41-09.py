class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram = {}

        for string in strs:
            s = "".join(sorted(string))

            if s not in anagram:
                anagram[s] = []
            anagram[s].append(string)
        return list(anagram.values())
