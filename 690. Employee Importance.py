"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        emp_map = {emp.id: emp for emp in employees}
        queue = [id]
        total = 0

        while queue:
            emp_id = queue.pop(0)
            emp = emp_map[emp_id]
            total += emp.importance

            for e in emp.subordinates:
                queue.append(e)

        return total
