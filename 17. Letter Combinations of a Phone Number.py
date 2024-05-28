class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        if not digits:
            return []

        output = ['']

        for digit in digits:
            temp = []
            for combination in output:
                for letter in mapping[digit]:
                    temp.append(combination + letter)

            output = temp

        return output
