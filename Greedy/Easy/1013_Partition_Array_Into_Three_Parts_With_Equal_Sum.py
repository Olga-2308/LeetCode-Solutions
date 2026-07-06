class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        '''
        Since it is necessary to find three non-empty arrays with the same sum, 
        this means that the sum of the array must be a multiple of three, 
        and then it is necessary each time to determine the array 
        whose sum is equal to one third of the total sum of the array.
        '''

        # We determine the sum of the entire array, and if the sum is not divisible by 3 without a remainder, 
        # then this means that it is impossible to create three arrays with the same sum and we return false
        total = sum(arr)
        if total % 3 != 0:
            return False

        # we determine the required sum of one subarray
        one_part = total // 3

        # We create counters, where one will accumulate the sum of the subarray to the required value, 
        # and the second will count the number of subarrays
        current = 0
        counter = 0

        # we begin to accumulate the sum of numbers using a loop
        for num in arr:
            current += num

            # If the current amount is equal to one third of the total amount, 
            # then one subarray is formed and we add it to the counter 
            # and start accumulating the amount again for the second array
            if current == one_part:
                counter += 1
                current = 0

        # If the result is 3 arrays, then we return true, otherwise false
        return counter == 3