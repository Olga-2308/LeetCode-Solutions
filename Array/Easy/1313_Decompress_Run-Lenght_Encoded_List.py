class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:

        # create an empty list to enter the result
        result = []

        # ''' In order for us to work in a loop alternately with a pair of elements, 
        # we specify that the index movement will be carried out in increments of two '''
        for i in range(0, len(nums), 2):

            # create variables and assign them the values ​​of adjacent elements accordingly
            freq = nums[i]
            val = nums[i+1]

            # create a list as specified in the problem statement
            part = [val] * freq

            # add elements to the list in order
            result.extend(part)
            
        return result