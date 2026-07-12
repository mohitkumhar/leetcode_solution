class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        map = {
            0: 'z',
            1: 'y',
            2: 'x',
            3: 'w',
            4: 'v',
            5: 'u',
            6: 't',
            7: 's',
            8: 'r',
            9: 'q',
            10: 'p',
            11: 'o',
            12: 'n',
            13: 'm',
            14: 'l',
            15: 'k',
            16: 'j',
            17: 'i',
            18: 'h',
            19: 'g',
            20: 'f',
            21: 'e',
            22: 'd',
            23: 'c',
            24: 'b',
            25: 'a'
        }

        result = []
        for word in words:
            curr_char = 0
            for char in word:
                curr_char += weights[ord(char) - ord("a")]
                curr_char = curr_char % 26

            result.append(curr_char)

        for i in range(len(result)):
            result[i] = map[result[i]]

        return "".join(result)
