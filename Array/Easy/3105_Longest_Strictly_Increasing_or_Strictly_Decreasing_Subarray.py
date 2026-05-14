class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        '''
        The beginning of an ascending sequence is the interruption of a descending sequence and vice versa
        '''

        # We set up counters to count the length of both subarrays. 
        # Since the first element is always included in the subarray, counting starts at 1.
        up = 1
        cur_up = 1

        down = 1
        cur_down = 1

        # Using a loop, we check each number in turn with its neighbor and determine the type of the sequence 
        # (since pairs of numbers are compared, we specify -1)
        for i in range(len(nums) - 1):

            # If the current number is less than the next number, then the sequence is increasing. 
            # We increment the counter of the increasing sequence and reset the counter of the decreasing sequence to 1, 
            # since it terminated at this iteration.
            if nums[i] < nums[i+1]:
                cur_up += 1
                cur_down = 1

                # we determine the maximum length
                if cur_up > up:
                    up = cur_up

            # We do the same for the decreasing sequence, 
            # only in this case the increasing sequence is interrupted
            elif nums[i] > nums[i+1]:
                cur_down += 1
                cur_up = 1

                if cur_down > down:
                    down = cur_down

            # If the numbers are equal, then both sequences are interrupted and we will reset the counters to 1, 
            # so it is necessary to find the lengths of strictly increasing and strictly decreasing subarrays
            elif nums[i] == nums[i+1]:
                cur_up = 1
                cur_down = 1

        # return the maximum length
        return max(up, down)