class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPal(nums, i, j):
            return nums[i : j + 1] == nums[i : j + 1][::-1]

        def backtrack(i: int, temp: List[int]):
            if i == n:
                result.append(temp[:])
                return

            for j in range(i, n):
                if not isPal(s, i, j):
                    continue

                temp.append(s[i : j + 1])

                backtrack(j + 1, temp)

                temp.pop()

        result = []
        n = len(s)
        backtrack(0, [])

        return result
