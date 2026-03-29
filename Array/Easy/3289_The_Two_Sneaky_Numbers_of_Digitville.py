class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

        # create an empty list to add one of the paired numbers
        result = []

        # sort the list so that identical numbers are next to each other
        nums.sort()

        # create a loop in which we work with each number. 
        # Since we are considering pairs of numbers, we specify -1 in the final boundary so that the last pair is: 
        # the second-to-last number and the last
        for i in range(0, len(nums)-1):

            # If the current number is equal to the next number, then add this number to the list. 
            # Since duplicates only appear twice in the list, there will be only one pair of identical numbers. 
            # (1223 --> 1-2, 2-2, 2-3 - one pair)
            if nums[i] == nums[i+1]:
                result.append(nums[i])

        return result