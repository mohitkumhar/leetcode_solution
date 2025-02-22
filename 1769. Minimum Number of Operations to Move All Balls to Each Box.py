class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = []

        for i in range(len(boxes)):
            j = 0
            temp = []
            while j < len(boxes):
                if i == j:
                    j += 1
                    continue
                if boxes[j] == '0':
                    j+=1
                    continue

                temp.append(abs(i - j))
                j += 1
            result.append(sum(temp))
        
        return result
        