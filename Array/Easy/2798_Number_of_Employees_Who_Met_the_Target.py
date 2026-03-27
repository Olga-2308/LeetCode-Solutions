class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        
        # create a counter to count the number of employees who work the standard or overtime hours
        counter = 0

        # create a cycle in which we work with the working hours of each employee
        for employee in hours:

            # If the employee's working hours are greater than or equal to the established norm, the counter increases by 1
            if employee >= target:
                counter += 1

        return counter