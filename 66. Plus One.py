class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        answer = []
        number = ''

        for digit in digits:
            number += str(digit)        
        number = str(int(number) + 1)

        for num in number:
            answer.append(int(num))
        return answer
