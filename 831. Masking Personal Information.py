class Solution:
    def maskPII(self, s: str) -> str:
        def clean_email(email):
            email = email.lower()
            email = email.split('@')
            email[0] = email[0][0] + '*****' + email[0][-1]
            
            return email[0] + '@' + email[-1]

        def clean_number(numbers):
            digits = [c for c in numbers if c.isdigit()]
            country_code = len(digits) - 10
            local = ''.join(digits[-4:])

            if country_code == 0:
                return '***-***-' + str(local)
            else:
                return '+' + '*' * country_code + '-***-***-' + str(local)


        if '@' in s:
            return clean_email(s)
        
        else:
            return clean_number(s)
        