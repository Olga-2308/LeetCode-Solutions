class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:

        '''
        To determine the size of the prefix to be removed, we need to check the sequence from the end. 
        Once the numbers stop descending (comparing from the end), we return the index, which is the length of the prefix.
        '''
        
        # We create a loop that starts from the end:
            # [len(nums) - 1] - the loop starts with the last element, 
            # and since indexing starts from zero, we decrease the number by 1

            # [0] - with the end of the loop at 0, the last iteration will be at the number with index 1 
            # (the second-to-last element, which will be added to the last)

            # [-1] - with a step of -1, the loop goes in reverse order       
        
    
        for i in range(len(nums) - 1, 0, -1):

            # if the current number has become less than or equal to the previous one 
            # (the next one in reverse order), then we return the index
            if nums[i] <= nums[i-1]:
                return i

        # If the entire sequence is increasing, then there is no need to delete anything and we return 0
        return 0