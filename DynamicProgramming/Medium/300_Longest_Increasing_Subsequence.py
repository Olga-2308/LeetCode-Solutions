class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # immediately return 1 if the array length is 1
        l = len(nums)
        if l == 1:
            return 1

        # Using the set, we determine whether the array consists of identical numbers. 
        # If so, we return 1, since identical numbers do not satisfy the condition of a strictly increasing sequence.
        if len(set(nums)) == 1:
            return 1

        # we create an array to store the number of possible sequences for each number in the original array
        dp = [1] * l

        # Using a loop, we begin to count the number of possible sequences for each number. 
        # Since the first element of the array always has a sequence of length 1, 
        # we begin iterations from the second element (1 by index)
        for i in range(1, l):

            # We need to determine how many numbers from 0 to the current number can be included in the desired sequence. 
            # To do this, we run an inner loop that compares the current number 
            # with the numbers in the array from 0 to the current number in the outer loop.
            for j in range(i):

                # If the current loop number is greater than the number of the inner loop 
                # (the left side of the array), this means that the current number 
                # may be part of a strictly increasing sequence
                if nums[i] > nums[j]:

                    # Now we need to determine the maximum sequence length for the current number in the array in the memory array. 
                    # To do this, we compare the current value in memory (initially it is 1, 
                    # but can change during the loop), and the second number is the maximum possible 
                    # current sequence length of the number from the left side of the loop (inner), 
                    # which was found earlier, plus 1, since the current number of the outer loop is also added to the new sequence.
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)