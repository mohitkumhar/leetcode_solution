class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        counter = {}

        for i, char in enumerate(word):
            if char.islower():
                if char not in counter:
                    counter[char] = i
                counter[char] = i

            else:
                if char not in counter:
                    counter[char] = i

        count = 0
        for key, value in counter.items():

            if key.islower():
                if key.upper() in counter:
                    if counter[key] - counter[key.upper()] < 0:
                        count += 1

        return count
