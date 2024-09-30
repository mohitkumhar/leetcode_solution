class Solution:
    def reformat(self, s: str) -> str:
        number = []
        character = []

        for i in s:
            if i.isalpha():
                character.append(i)
            else:
                number.append(i)
        
        if abs(len(number) - len(character)) > 1:
            return ''

        
        if len(number) > len(character):
            number, character = character, number
        

        ans = []
        
        for i in range(len(character)):
            ans.append(character[i])
            if i < len(number):
                ans.append(number[i])
        
        return ''.join(ans)

                


