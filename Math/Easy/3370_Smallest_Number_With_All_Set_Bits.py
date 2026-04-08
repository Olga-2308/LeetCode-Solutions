class Solution:
    def smallestNumber(self, n: int) -> int:

        # All powers of two in binary form have the following form:

            # 1 = 001               
            # 2 = 010               
            # 4 = 100               --> (3) = 11
            # 8 = 1000              --> (7) = 111
            # 16 = 10000            --> (15) = 1111
            # 32 = 100000           --> (31) = 11111
            # 64 = 1000000          --> (63) = 111111
            # 128 = 10000000        --> (127) = 1111111
        
        # And all numbers that are 1 less than a power of two contain only ones in binary form.
        # Therefore, to find such a number with all 1's, it is necessary to determine the nearest number that is a power of two and subtract 1 from it.

        # Let's start checking all the degrees from the beginning until the number exceeds n
        x = 0
        
        # we find the result of the current power of two without 1
        while (2 ** x) - 1 < n:

            # If we haven't reached the maximum possible value, then we increase the degree by 1 and continue checking
            x += 1 
            
        # We return the resulting number and subtract one from it, 
        # since it is the previous number that has 1 in all digits of the binary number.
        return (2 ** x) - 1