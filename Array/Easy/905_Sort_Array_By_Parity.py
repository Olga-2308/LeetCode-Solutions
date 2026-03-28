class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        # create two lists, for even and odd numbers
        even = []
        odd = []

        # create a loop in which we work with each number in order
        for num in nums:

            # if a number is divisible by 2 without a remainder, then it is even, and we add it to the corresponding list
            if num % 2 == 0:
                even.append(num)

            # otherwise add the number to the list for odd numbers
            else:
                odd.append(num)

        # combine two lists, where even numbers come first, then odd ones
        result = even + odd

        return result