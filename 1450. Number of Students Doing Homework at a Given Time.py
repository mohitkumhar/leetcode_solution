class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        
        i = 0
        j = 0

        result = 0

        while i != len(startTime):

            if startTime[i] <= queryTime and queryTime <= endTime[j]:
                result += 1
                print('startTime[i] is: ', startTime[i])
                print('endTime[i] is: ', endTime[i])
                print()

            i += 1
            j += 1
        
        return result
