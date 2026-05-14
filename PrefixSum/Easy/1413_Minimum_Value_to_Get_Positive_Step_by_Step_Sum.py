class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        '''
        Let's start the check with the minimum acceptable value and find the total sum. 
        Then, we'll determine the minimum value in the step and increase the target value 
        by the minimum required value so that there are no negative numbers in the intermediate steps.
        '''

    
        # the first minimum number to check is 1 (the condition requires a positive number)
        startValue = 1
        value = 0

        # we set the minimum result value to a positive infinite number 
        # so that any first value obtained is guaranteed to be less than the value of the variable
        min_result = float("inf")

        # Using a loop, we add the values ​​from the array one by one
        for num in nums:
            value += num

            # and at each step we determine the minimum value
            if value < min_result:
                min_result = value

        # If the minimum value is greater and equal to 1, 
        # this means that the intermediate calculations do not go beyond the established limits 
        # and the value of the variable equal to 1 is suitable for us.
        if min_result >= 1:
            return startValue
        
        # If during the calculations there was a negative number at an intermediate step, 
        # then at a minimum it is necessary to increase the value by the absolute value of this number 
        # in order to get out of negative numbers and add 1 so that the step is not less than 1 (according to the problem statement)
        else:
            startValue = abs(min_result) + 1
            return startValue