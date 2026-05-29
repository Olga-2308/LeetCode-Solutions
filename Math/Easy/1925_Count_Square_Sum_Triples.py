class Solution:
    def countTriples(self, n: int) -> int:

        counter = 0
        sqrt = set()

        # I create a set of squares from all possible numbers in the range from 1 to n
        for i in range(1, n+1):
            sqrt.add(i ** 2)

        # using a nested loop, find non-repeating pairs of numbers 
        # whose sum of squares does not exceed the square of the maximum value of a given number
        for i in range(1, n - 1):
            for j in range(i+1, n):

                # Once such a pair has been found, 
                # it is necessary to check whether there is a square of the sum of two numbers in the created set, 
                # and if there is, then the conditions of the given expression are met, and we increase the counter
                if (i ** 2) + (j ** 2) <= n ** 2 and (i ** 2) + (j ** 2) in sqrt:
                    counter += 1

        # since the order of the terms does not change the value of the sum 
        # and there is no strict limitation on the indices, 
        # it is possible to compose twice as many pairs (triplets) of numbers where the terms change places
        return counter * 2