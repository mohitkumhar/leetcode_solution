class Solution:
    def reformatNumber(self, number: str) -> str:
        number = ''.join([i for i in number if i.isnumeric()])
        ans = ''

        while len(number) > 4:
            ans += number[:3] + '-'
            number = number[3:]
        
        if len(number) == 4:
            ans += number[:2] + '-' + number[2:] + '-'
            number = number[4:]
        
        if len(number) == 3:
            ans += number[:3] + '-'
            number = number[3:]
        
        if len(number) == 2:
            ans += number[:2] + '-'
            number = number[2:]
        
        return ans[:-1]
