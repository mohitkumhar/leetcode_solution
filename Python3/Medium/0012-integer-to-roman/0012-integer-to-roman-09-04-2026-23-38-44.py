class Solution:
    def intToRoman(self, num: int) -> str:

        values = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (3, "III"),
            (2, "II"),
            (1, "I"),
        ]

        ans = ""
        for value, symbol in values:
            while num >= value:
                num -= value
                ans += symbol

        return ans
