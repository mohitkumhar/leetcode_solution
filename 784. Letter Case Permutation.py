class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []

        def backtrack(index, sub_array):
            if index == len(s):
                result.append(sub_array)
                return
            
            elif s[index].isalpha():
                backtrack(index + 1, sub_array + s[index].upper())
                backtrack(index + 1, sub_array + s[index].lower())

            else:
                backtrack(index + 1, sub_array + s[index])

        backtrack(0, '')
        return result
