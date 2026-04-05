class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        # We check whether the given number is greater than 0 (the square of any number is always a positive number) 
        # and use bitwise check for power of two
        if n > 0 and n & (n-1) == 0:
            return True
        else:
            return False
        
    
# Let's take a closer look at this expression n & (n-1) == 0
# If the bitwise AND between a given number and a number less than one results in 0, 
# then this means that there was only one 1 in the given number. Therefore, this number is a power of two.
 
# Powers of two have the following binary form:
 
    # 1 - 1
    # 2 - 10
    # 4 - 100
    # 8 - 1000
    # 16 - 10000
    # 32 - 100000
    # 64 - 1000000 
    # ...

# They all have one 1 in the highest digit. 
# And the AND operator helps determine whether a given number had one digit in the leading digit.
 
# For example, we are given the number 32, in binary form it looks like this: 100000
# It is necessary to determine the number that is less by one: 32 - 1 = 31
 
# 31 in binary form: 31 = 16 + 8 + 4 + 2 + 1 --> 11111  

# Now we check the expression n & (n-1) == 0:

    # 100000 (32)
    #  11111 (31)
    # ______
    # 000000 --> Got 0.
 
# This means that the given number in binary form had one 1 in the most significant digit, 
# hence the given number is a power of 2.