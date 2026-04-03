class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:

        # create variables to calculate the sum of even and odd numbers
        odd = 0
        even = 0

        # determine how many iterations are needed for the loop to count the specified number of numbers in each variable. o denotes the number of numbers in the sequence; since there are two sequences, we increase the number by 2 times.
        all = 2 * n

        # create a loop in which we calculate the sums of two sequences of numbers
        for i in range(1, all+1):

            # If the number is even, add it to one sequence
            if i % 2 == 0:
                even += i

            # if odd, then to the other
            else:
                odd += i

        # determine the minimum number. It can be the maximum common divisor for two numbers. 
        divisor = min(odd, even)

        # create a loop in which we find the maximum common divisor
        # check all the numbers from largest to smallest.
        while divisor != 0:

            # If both numbers are divisible by the current divisor without a remainder, then we return this number
            if odd % divisor == 0 and even % divisor == 0:
                return divisor
            
            # otherwise we decrease the divisor by 1 and continue checking
            else:
                divisor -= 1


# return n

# If you find the sum of the first odd numbers in a sequence, 
# you will always find the square of the number that is the number of those numbers in the sequence.

    # 1 + 3 + 5 = 9 (3**2 = 9)
    # 1 + 3 + 5 + 7 + 9 = 25 (5**2 = 25)
 
# If we find the sum of the first even numbers in a sequence, the result can be expanded as follows:

    # 2 + 4 + 6 = 12 (3 * (3+1)) - n**2
    # 2 + 4 + 6 + 8 + 10 = 30 (5 * (5+1)) n(n+1)
 
# To find the GCD, you need to find the greatest common factor.
# Both values ​​can be abbreviated by n
 
    # n**2 = n
    # n(n+1) = n + 1    

# any two consecutive prime numbers are relatively prime, 
# therefore they have no common divisors other than 1