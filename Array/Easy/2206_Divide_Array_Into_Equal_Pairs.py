class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        # The problem statement states that the list consists of an even number of numbers. 
        # The pairs must be arranged so that the numbers in the pairs are equal. 
        # To create equal pairs, the list must be sorted so that equal values ​​appear next to each other. 
        # Since we're assembling pairs, the number of equal numbers must be even, otherwise the problem statement won't be satisfied. 
        # If we assume an even number, then each pair will have equal values ​​when sorted.

        # sort the list so that the numbers are in the correct order
        nums.sort()

        # create a loop in which we check pairs of numbers. Since we need to check each pair, 
        # starting with indices 0, 2, 4, and so on, we set the loop to step 2.
        for i in range(0, len(nums)-1, 2):

            # If the numbers in the pair are not equal, then we immediately return false and terminate the loop.
            if nums[i] != nums[i+1]:
                return False

        # If after checking all pairs of numbers all values ​​are equal, then we return true
        return True