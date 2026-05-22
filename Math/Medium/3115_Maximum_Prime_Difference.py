class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        '''
        To find the maximum distance, you need to determine the first and last occurrence of a prime number in the array
        '''

        # create a set of prime numbers in the range from 1 to 100
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}

        # we define the first and last occurrences as -1 so as not to miss the value under index 0
        first = -1
        second = -1

        # using a loop, we search for prime numbers one by one
        for i in range(len(nums)):
            if nums[i] in primes:
                
                # Once you have found a prime number, you need to write down its index. 
                # If the first occurrence of the prime number has not yet occurred, 
                # then the current one will be the first number.
                if first == -1:
                    first = i   

                # We update the second number every time we encounter a prime number, 
                # since the distance between the farthest prime numbers is greater
                second = i      

        # return the difference in indices
        return second - first