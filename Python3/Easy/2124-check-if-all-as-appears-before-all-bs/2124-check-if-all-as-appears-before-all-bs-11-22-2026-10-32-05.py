class Solution:
    def checkString(self, s: str) -> bool:
        flag = False

        for char in s:
            if char == "b":
                flag = True

            if char == "a" and flag:
                return False
        return True
