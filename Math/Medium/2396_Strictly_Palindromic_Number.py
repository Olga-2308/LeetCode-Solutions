class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:

        # create a loop in which we go through each number system (Base)
        for i in range(2, n-1):

            # create a copy of the number so that the original remains unchanged
            cop_n = n

            # create a blank sheet to write the number in the modified number system
            current_num = []

            # We create a loop in which we transform each number. 
            # The loop continues until the number becomes 0.
            while cop_n != 0:

                # we divide the number by the index, which is the current base, 
                # and find the remainder from the division
                digit = cop_n % i

                # add the remainder to the list
                current_num.append(digit)

                # find the result of integer division and repeat the cycle until the number becomes equal to 0
                cop_n = cop_n // i

            # If the resulting list of numbers is not equal to the list in reverse form (the condition for a palindrome), 
            # then return false
            if current_num != current_num[::-1]:
                return False
            
        # If after checking all bases the numbers are palindromes, then return true
        return True
    

# The problem states that the condition is satisfied if all numbers are palindromes.
# This means that every number in every base must be a palindrome.
# The maximum base of a number is always 2 units less than the number itself (from the problem statement).
# Therefore, every time we analyze a number to its last base, we can take 1 whole and two remainder.
# The result will always be the number 12, which is not a palindrome:
# 23 to the base 21 (23-2) -->
    # 23 // 21 = 1 (from 23 you can take the number 21 only once)
    # 23% 21 = 2 (remainder from division)
# The resulting number is 12, which is not a palindrome. This is true for all numbers n >= 4 and base (n-2).


    
