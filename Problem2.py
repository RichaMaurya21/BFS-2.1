## Problem 2

#Employee Impotance(https://leetcode.com/problems/employee-importance/)

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        employeeMap = {}
        for emp in employees:
            employeeMap[emp.id] = emp
  
        res = 0
        q = deque([id])
        while q:            
            currentID = q.popleft()
            currentEmployee = employeeMap[currentID]
            res += currentEmployee.importance
            for subId in currentEmployee.subordinates:
                q.append(subId)

        return res

