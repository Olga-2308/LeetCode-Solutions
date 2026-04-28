class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:

        d = {}

        # We create a loop with which we create a dictionary based on a given array
        for num in nums:

            # Only even elements need to be added to the dictionary.
            if num % 2 == 0:
                if num not in d:
                    d[num] = 1
                else:
                    d[num] += 1

        # If the dictionary is empty, then there are no even numbers in the array and we return -1
        if len(d) == 0:
            return -1

        # We set a counter to find the maximum number
        f = 0

        # We set a counter to determine the minimum value
        result = -1

        # We create a loop in which we check each element of the dictionary
        for num in d:

            # First we determine the frequency of the number in the array, if it is greater than the set value, 
            # then we update the frequency counter and update the value in the final variable
            if d[num] > f:
                f = d[num]
                result = num

            # If the quantity turns out to be equal to the previously set maximum frequency value, 
            # then it is necessary to determine which of the numbers is smaller and return it
            elif d[num] == f:
                if num < result:
                    result = num

        return result