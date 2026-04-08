class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        for char in set(word1):
            if char not in word2:
                return False
        for char in set(word2):
            if char not in word1:
                return False
        
        if set(word1) != set(word2):
            return False

        counter1 = {}
        counter2 = {}

        for char in word1:
            if not char in counter1:
                counter1[char] = 0
            counter1[char] += 1

        for char in word2:
            if not char in counter2:
                counter2[char] = 0
            counter2[char] += 1

        return sorted(counter2.values()) == sorted(counter1.values())
