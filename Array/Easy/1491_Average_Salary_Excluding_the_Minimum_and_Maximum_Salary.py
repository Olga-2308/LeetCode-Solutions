class Solution:
    def average(self, salary: List[int]) -> float:

        '''
        We need to calculate the average salary, excluding the maximum and minimum values. 
        To do this, we sort the array and create a slice excluding two employees. 
        We update the divisor and find the average value using the formula
        '''
        
        # We sort the array to easily determine the maximum and minimum values
        salary.sort()

        # Since two employees are excluded, the divisor must be reduced by 2.
        div = len(salary) - 2

        # We define a new array of employees, excluding extremes
        employee = salary[1:-1]

        # we find the average value using the formula
        average = sum(employee) / div

        return average