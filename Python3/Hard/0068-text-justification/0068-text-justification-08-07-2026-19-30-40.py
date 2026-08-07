class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0
        n = len(words)

        while i < n:
            j = i
            currWordLength = 0

            while j < n:
                gaps = j - i
                if (currWordLength + len(words[j]) + gaps) > maxWidth:
                    break

                currWordLength += len(words[j])
                j += 1

            currWords = words[i:j]
            numberOfWords = len(currWords)

            gaps = numberOfWords - 1

            # if it is last line of there is only one word
            if j == n or numberOfWords == 1:
                line = " ".join(currWords)
                line += " " * (maxWidth - len(line))

            else:
                totalSpaces = maxWidth - currWordLength
                evenSpaces = totalSpaces // gaps
                extraSpaces = totalSpaces % gaps

                line = ""

                for k in range(gaps):
                    line += currWords[k]
                    line += " " * evenSpaces

                    if k < extraSpaces:
                        line += " "

                line += currWords[-1]

            result.append(line)
            i = j

        return result
