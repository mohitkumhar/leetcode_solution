class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absent = 0
        late = 0


        for i in s:

            if i == 'A':
                late = 0
                absent += 1
            
            elif i == 'L':
                late += 1
            
            elif i == 'P':
                late = 0

            if absent >= 2:
                return False
            
            if late >= 3:
                return False
        
        return True
        