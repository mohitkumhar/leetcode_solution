class Solution:
    def maxLength(self, arr: list[str]) -> int:

        def isDuplicate(str1, str2):
            strs = [0] * 26

            for char in str1:
                idx = ord(char) - ord("a")
                strs[idx] += 1
                if strs[idx] > 1:
                    return True
            for char in str2:
                idx = ord(char) - ord("a")
                strs[idx] += 1
                if strs[idx] > 1:
                    return True
            return False

        def solve(i, currStr):
            if i >= n:
                return len(currStr)

            include = 0
            exclude = 0

            if isDuplicate(currStr, arr[i]):
                exclude = solve(i + 1, currStr)
            else:
                include = solve(i + 1, currStr + arr[i])
                exclude = solve(i + 1, currStr)

            return max(include, exclude)

        n = len(arr)
        currStr = ""
        return solve(0, currStr)
