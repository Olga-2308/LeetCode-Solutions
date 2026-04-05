class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # create a variable in which we will search for a number without a pair
        result = 0

        # create a loop in which we go through each number
        for num in nums:

            # Using the XOR operator, we find a number that does not have its own identical pair.
            result = result ^ num

        return result
    

# When using the bitwise XOR operator, identical numbers in binary form return 0.
# For example, the number n = 27:
            # 16 + 8 + () + 2 + 1 = 11011
 
# n ^ n 
 
    #  11011
    #  11011
    #  -----
    #  00000  --> We got 0, therefore the numbers are equal.

# Consider the list of numbers nums = [4,1,2,1,2]
# To work with each number, a loop is created:
    
# Numbers in binary form have the following form:
 
    # 1 - 001
    # 2 - 010
    # 4 - 100
 
# The variable at the beginning of the loop is equal to 0.
# Let's start working with the first number:
 
# i = 0, num[i] = 4
 
    # 000 (result = 0)
    # 100 
    # ---
    # 100

# i = 1, num[i] = 1

    # 100
    # 001
    # ---
    # 101

# i = 2, num[i] = 2

    # 101
    # 010
    # ---
    # 111

# i = 3, num[i] = 1

    # 111
    # 001
    # ---
    # 110

# i = 4, num[i] = 2

    # 110
    # 010
    # ---
    # 100 - We got the number 4, the only number without a pair.
