class Solution:
    def findMaxK(self, nums: List[int]) -> int:

        # Since we need to find the maximum number that satisfies the problem conditions, 
        # we need to sort the list in descending order. 
        # As soon as the maximum suitable number is found, the loop will terminate.
        nums.sort(reverse = True)

        # create a loop in which we check each number, starting with the maximum
        for num in nums:

            # If the same number, but in the negative range, is in the same array, 
            # then we return this positive number and terminate the loop, since the maximum number has been found
            if num * (-1) in nums:
                return num
           
        # If after checking all the numbers, nothing is found, then we return -1
        return -1
    
        #  if num * (-1) in nums and num > 0:
        # You can also add to the condition that the number must be positive, 
        # so that if there are no suitable numbers, the loop does not check for negative values.