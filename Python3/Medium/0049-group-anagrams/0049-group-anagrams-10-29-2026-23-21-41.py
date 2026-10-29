class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        counter = {}

        for word in strs:
            sortedWord = "".join(sorted(word))
            print(sortedWord)

            if sortedWord not in counter:
                counter[sortedWord] = []
            counter[sortedWord].append(word)

        return list(counter.values())
