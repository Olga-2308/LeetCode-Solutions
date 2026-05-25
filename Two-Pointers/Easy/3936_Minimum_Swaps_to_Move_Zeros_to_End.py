class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:

        # We define the start of the pointers and create a counter for the number of exchanges
        i = 0
        j = len(nums) - 1
        counter = 0

        while i < j:

            # If the pointers are at 0 and not at 0 respectively, 
            # then an exchange can be made, so we increment the counter 
            # and move the pointers one step towards the center
            if nums[i] == 0 and nums[j] != 0:
                counter += 1
                i += 1
                j -= 1

            # we move the left pointer until we encounter 0, 
            # because only in this case can we make an exchange
            elif nums[i] != 0:
                i += 1

            # We move the right pointer towards the center until we encounter a number starting from 0, 
            # because only in this case can we put 0 in this place
            elif nums[j] == 0:
                j -= 1

        return counter