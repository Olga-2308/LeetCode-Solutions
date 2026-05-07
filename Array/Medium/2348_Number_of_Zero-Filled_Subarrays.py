class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        counter = 0
        current = []

        # using a loop we search for all sequences of zeros
        for num in nums:

            # If the number is 0, we immediately add it to the array. 
            # To determine how many subarrays can be created, we need to find the array's length, 
            # which is the number of subarrays. For example, with one zero, only one subarray is possible: [0]. 
            # If the array has two zeros, then two subarrays can be created: [0] and [00], and so on.
            if num == 0:
                current.append(0)
                counter += len(current)

            # As soon as we encounter a number other than 0, 
            # the sequence is interrupted and we start looking for a new one
            else:
                current = []

        return counter