class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def get_waviness(string):
            score = 0
            for i in range(1, len(string) - 1):
                if string[i - 1] < string[i] > string[i + 1]:
                    score += 1
                elif string[i - 1] > string[i] < string[i + 1]:
                    score += 1
            return score

        score = 0
        for num in range(num1, num2 + 1):
            string = str(num)
            score += get_waviness(string)

        return score
