class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(i, curr_comb):
            nonlocal result
            if i >= len(nums):
                result.append("".join(curr_comb))
                return


            for j in range(len(nums[i])):
                curr_comb.append(nums[i][j])

                backtrack(i + 1, curr_comb)

                curr_comb.pop()


        map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        nums = []

        for digit in digits:
            nums.append(map[digit])
        
        result = []

        backtrack(0, [])

        return result
