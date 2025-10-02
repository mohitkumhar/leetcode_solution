class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        mapping = {k: v for k, v in knowledge}
        
        bracket = False
        result = []
        temp = []
        for char in s:
            if char == '(':
                bracket = True
                continue
            elif char == ')':
                bracket = False
                key = ''.join(temp)
                word = mapping.get(key, '?')
                result.append(word)
                temp = []
                continue
            if bracket:
                temp.append(char)
                continue
            else:
                result.append(char)

        return ''.join(result)
