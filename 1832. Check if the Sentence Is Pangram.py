class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        map = {}
        for char in sentence:
            if char not in map:
                map[char] = 0
            map[char] += 1
        return len(map) == 26
