class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        def check(num, number):
            number = list(number)
            for i in str(num):
                if int(i) in number:
                    number.remove(int(i))
                else:
                    return False
            return True

        result = []
        for i in range(100, 999):
            if i % 2 == 0:
                if check(i, digits):
                    result.append(i)
        return result
