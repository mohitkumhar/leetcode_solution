class Solution:
    def compress(self, chars: List[str]) -> int:
        idx = 0
        n = len(chars)
        i = 0
        ans = []
        while i < n:
            count = 1
            temp = i

            ans.append(chars[i])
            while temp < n-1:
                if chars[temp] == chars[temp + 1]:
                    count += 1
                else:
                    break
                temp += 1
            if count > 1:
                ans.extend(list(str(count)))
            i = temp

            i += 1

        chars[:] = ans
