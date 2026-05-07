class Solution:
    def kthFactor(self, n: int, k: int) -> int:

        factors = []

        # using a loop we generate numbers from 1 (cannot be divided by 0) to n.
        for i in range(1, n+1):

            # we add to the array all numbers that are divisors of a given number
            if n % i == 0:
                factors.append(i)

        # Since an element with a specific number is required, 
        # it is necessary to check whether this serial number is in the array itself 
        # and if it is not present, return -1
        if len(factors) >= k:
            return factors[k-1]
        else:
            return -1