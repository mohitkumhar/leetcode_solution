class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        seen = set()
        for word in words:
            even = ''.join(sorted(word[::2]))
            odd = ''.join(sorted(word[1::2]))
            seen.add((odd, even))
        return len(seen)