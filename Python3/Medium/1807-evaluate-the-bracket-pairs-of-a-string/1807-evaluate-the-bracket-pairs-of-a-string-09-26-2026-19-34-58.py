class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        counter = {}

        for key, value in knowledge:
            counter[key] = counter.get(key, "") + value

        flag = False
        curr = ""
        ans = ""

        for char in s:
            if char == "(":
                flag = True
                curr = ""

            elif char == ")":
                ans += counter.get(curr, "?")
                curr = ""
                flag = False

            elif flag:
                curr += char

            else:
                ans += char

        return ans
