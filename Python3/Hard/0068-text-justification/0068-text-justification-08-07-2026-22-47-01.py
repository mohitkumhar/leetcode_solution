class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        result = []
        i = 0
        n = len(words)

        while i < n:
            j = i
            totalWordsLength = 0
            gaps = 0

            while j < n and (totalWordsLength + len(words[j]) + gaps) <= maxWidth:
                totalWordsLength += len(words[j])
                j += 1
                gaps = j - i

            currWords = words[i:j]
            numberOfWords = len(currWords)
            gaps = numberOfWords - 1

            # if i am on last line or we just have one word in a line
            if j == n or numberOfWords == 1:
                line = " ".join(currWords)
                line += " " * (maxWidth - len(line))

            else:
                line = ""

                availableSpaces = maxWidth - totalWordsLength
                evenSpaces = availableSpaces // gaps
                extraSpaces = availableSpaces % gaps

                for k in range(gaps):
                    line += currWords[k]
                    line += " " * evenSpaces

                    if k < extraSpaces:
                        line += " "

                line += currWords[-1]

            result.append(line)
            i = j

        return result
