class Solution:
    def oddString(self, words: List[str]) -> str:
        difference = []
        n = len(words)
        for w in words:
            diff = []
            for j in range(len(w) - 1):
                diff.append(ord(w[j+1]) - ord(w[j]))
            difference.append(tuple(diff))
        unique = []

        for index, diff in enumerate(difference):
            counter = 0
            for count in difference:
                if count == diff:
                    counter += 1

            if counter == 1:
                return words[index]
