class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        # create lists for numbers and zeros to create a list according to the problem statement.
        digit = []
        zero = []

        # We create a loop in which we check pairs of numbers. 
        # Since two numbers in a row are checked, 
        # we reduce the length of the loop by 1 so as not to go beyond the limits.
        for i in range(len(nums)-1):

            # It is necessary to determine whether the current number is equal to the next one in the array. 
            # If the numbers are equal, then:
            if nums[i] == nums[i+1]:

                # the current number is multiplied by 2
                nums[i] = nums[i] * 2

                # the next number is assigned a new value of 0
                nums[i+1] = 0

        # After we've received a new array of numbers, we need to ensure that the numbers in it are in a specific order. 
        # To do this, we create a loop in which we iterate over each number in the array.
        for num in nums: 

            # If the number is 0, we add it to the corresponding list
            if num == 0:
                zero.append(num)
            
            # otherwise we add the number to the second list
            else:
                digit.append(num)

        # After this, we combine the two lists so that the zeros are at the end
        result = digit + zero
        
        return result