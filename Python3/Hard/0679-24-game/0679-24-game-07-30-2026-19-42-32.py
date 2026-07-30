class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:

        def backtrack(cards):
            if len(cards) == 1:
                print(abs(cards[0]), abs(cards[0] - 24))
                return abs(cards[0] - 24) < 1e-6

            n = len(cards)
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    temp = []
                    for k in range(n):
                        if k != i and k != j:
                            temp.append(cards[k])

                    a = cards[i]
                    b = cards[j]

                    result = [a + b, a - b, b - a, a * b]

                    if a != 0:
                        result.append(b / a)
                    if b != 0:
                        result.append(a / b)

                    for res in result:
                        temp.append(res)
                        if backtrack(temp):
                            return True
                        temp.pop()
            return False

        if backtrack(cards):
            return True
        return False
