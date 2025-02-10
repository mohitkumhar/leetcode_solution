class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1,1]]
        result = [[1], [1, 1]]
        
        k = 1
        while k < numRows - 1:
            i = 0
            temp = [1]
            while i+1 < len(result[k]):
                temp.append(result[k][i] + result[k][i + 1])
                i+=1
            temp.append(1)
            print(temp)
            print()
            result.append(temp)
            
            k+=1
        return result
        