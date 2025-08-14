class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ['999', '888', '777', '666', '555', '444', '333', '222', '111', '000']
        for a in ans:
            if a in num:
                return a
        return ''