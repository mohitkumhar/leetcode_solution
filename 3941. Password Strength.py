class Solution:
    def passwordStrength(self, password: str) -> int:

        special_set = set("!@#$")
        special = set()
        lower_char = set()
        upper_char = set()
        number = set()
        strength = 0

        for char in password:
            if char.isdigit():
                number.add(char)
            elif char.islower():
                lower_char.add(char)
            elif char.isupper():
                upper_char.add(char)
            else:
                special.add(char)

        return (
            len(lower_char) * 1 + 
            len(upper_char) * 2 + 
            len(number) * 3 + 
            len(special) * 5
        )
