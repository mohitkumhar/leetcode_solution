class Solution:
    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:

        def backtrack(i, currScore, freq) -> None:
            nonlocal bestScore
            bestScore = max(bestScore, currScore)
            if i >= len(words):
                return

            # take
            j = 0
            tempScore = 0
            tempFreq = freq.copy()

            while j < len(words[i]):
                char = words[i][j]

                tempScore += score[ord(char) - 97]
                tempFreq[ord(char) - 97] -= 1

                if tempFreq[ord(char) - 97] < 0:
                    break

                j += 1

            if j == len(words[i]):
                # take
                backtrack(i + 1, currScore + tempScore, tempFreq)

            # skip
            backtrack(i + 1, currScore, freq)

        freq = [0] * 26

        for letter in letters:
            freq[ord(letter) - 97] += 1

        bestScore = 0
        backtrack(0, 0, freq)

        return bestScore
