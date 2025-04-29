class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        common = set()
        seen = set()
        result = []
        count = 0

        for a, b in zip(A, B):
            for num in (a, b):
                print(num)
                if num in seen:
                    common.add(num)
                else:
                    seen.add(num)
                
            count = len(common)
            result.append(count)
    
        return result
