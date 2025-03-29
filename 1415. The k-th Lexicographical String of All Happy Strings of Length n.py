class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        happy_string = []

        def generate(curr):
            if len(curr) == n:
                happy_string.append(''.join(curr))
                return
            
            for char in 'abc':
                if not curr or curr[-1] != char:
                    generate(curr + [char])

        generate([])

        return happy_string[k - 1] if len(happy_string) >= k else  ''

