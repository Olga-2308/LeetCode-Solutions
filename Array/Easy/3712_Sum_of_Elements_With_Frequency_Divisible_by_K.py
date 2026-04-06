class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:

        # create a variable in which we will calculate the sum of all the suitable numbers
        total = 0

        # create a loop in which we check each number, 
        # since the condition says that it is necessary to add up all the numbers whose frequency satisfies the divisibility condition
        for num in nums:

            # If the frequency of a number occurs in the list in such a way that it is divisible by K without a remainder, 
            # then we add this number to the common variable
            if nums.count(num) % k == 0:
                total += num

        return total