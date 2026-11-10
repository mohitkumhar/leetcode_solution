class Solution:
    def replaceNonCoprimes(self, nums: list[int]) -> list[int]:
        stack = []

        for num in nums:

            while stack and gcd(stack[-1], num) > 1:
                num1 = num
                num2 = stack.pop()

                num = lcm(num1, num2)

            stack.append(num)

        return stack
