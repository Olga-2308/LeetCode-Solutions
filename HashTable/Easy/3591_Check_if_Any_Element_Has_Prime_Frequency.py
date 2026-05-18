class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:

        d = {}

        # we determine the frequency of each number in the array
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        # We check each frequency in the dictionary; 
        # if the frequency is less than 2, we skip it, 
        # since we need to find a value strictly greater than 1.
        for freq in d.values():
            if freq < 2:
                continue

            # We begin checking the expected divisors of the number, 
            # and define the minimum divisor as 2 to exclude division of the number by 1.
            div = 2

            # We check the divisors until the value is less than the frequency value, 
            # while excluding the divisor of the number by itself
            while div < freq:

                # Once we have found the first divisor, 
                # we stop the loop and move on to the next frequency, 
                # since the current value is not a prime number
                if freq % div == 0:
                    break 
                div += 1

            # If after checking all potential divisors we have not found any, 
            # then the number is prime and we return true
            else:
                return True

        # If no simple frequency values ​​are found, then return false
        return False