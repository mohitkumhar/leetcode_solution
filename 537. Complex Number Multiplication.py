class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parse_complex(s):
            parts = s.split('+')
            real = int(parts[0])
            imag = int(parts[1][:-1])
            return real, imag

        a, b = parse_complex(num1)
        c, d = parse_complex(num2)

        real_part = a * c - b * d # used '-' because i^2 is -1
        imag_part = a * d + b * c # cross multiplication is used to get imag part

        return str(real_part) + '+' + str(imag_part) + 'i'
