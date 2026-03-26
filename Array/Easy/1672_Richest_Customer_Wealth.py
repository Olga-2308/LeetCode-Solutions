class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        # create a variable to record the maximum result
        max_result = 0
        
        # create a loop in which we work with each element in order
        for customer in accounts:

            # find the sum of the numbers
            result = sum(customer)

            # If the sum is greater than the value in the variable max_result, then we assign a new value to the variable max_result
            if result > max_result:
                max_result = result

        return max_result