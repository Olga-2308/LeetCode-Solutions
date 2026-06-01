class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        '''
        To determine the minimum number of operations, 
        it is necessary to return the length of the set from the array not including 0. 
        Since at least 1 operation is needed for each distinct positive number in the array
        '''

        n = set(nums)

        if 0 in n:
            return len(n) - 1
        else:
            return len(n)
        
        '''
        counter = 0

            # We sort the array to immediately take the minimum values, 
            # as specified in the problem statement.
        nums.sort()

            # We create a variable in which we will store the accumulated difference. 
            # Since each iteration decreases each subsequent positive number
        total_diff = 0

            # using a loop we determine how much each number decreases from the previous values, 
            # and how much it will subtract from the following ones
        for i in range(len(nums)):
        
                # If the number is 0, then no additional operations need to be performed with it
            if nums[i] == 0:
                continue
            else:
            
                    # If the number is not 0, we must first determine what it is after subtracting all previous values. 
                    # To do this, we subtract the accumulated difference and select the maximum value. 
                    # If the difference is negative, we select 0, since we must reduce the number strictly to 0.
                nums[i] = max(0, nums[i] - total_diff)

                    # If after subtracting the accumulated difference the number is still greater than 0, 
                    # then we reduce this number to zero and add its value to the accumulated difference, 
                    # since all subsequent numbers after it must also be reduced by the value 
                    # of the current number in the cycle
                if nums[i] > 0:
                    total_diff += nums[i]
                    counter += 1
                    
        return counter
        '''