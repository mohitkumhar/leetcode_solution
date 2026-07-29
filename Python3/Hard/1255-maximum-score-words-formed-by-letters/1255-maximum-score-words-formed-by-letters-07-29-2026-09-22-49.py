class Solution:
    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:

        def backtrack(i, curr_score, freq):
            nonlocal count

            count = max(count, curr_score)
            if i >= len(words):
                return

            # skip
            backtrack(i + 1, curr_score, freq)

            # take
            j = 0
            m = len(words[i])
            temp_freq = freq.copy()
            temp_score = 0

            while j < m:
                char = ord(words[i][j])
                temp_freq[char - 97] -= 1
                temp_score += score[char - 97]

                if temp_freq[char - 97] < 0:
                    break

                j += 1

            if j == m:
                # take
                backtrack(i + 1, curr_score + temp_score, temp_freq)

        count = 0
        freq = [0] * 26
        for letter in letters:
            freq[ord(letter) - 97] += 1

        print(freq)

        backtrack(0, 0, freq)

        return count
