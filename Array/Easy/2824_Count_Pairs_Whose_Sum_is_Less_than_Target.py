class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:

        # create a counter to count the pairs found
        counter = 0
        
        # create a nested loop, where in the first loop we go through all the numbers in order
        for i in range(len(nums)):

            # In the second cycle, we begin working with numbers with a step of +1. 
            # In this case, we avoid repeating pairs and working with numbers on themselves. 
            for j in range(i+1, len(nums)):
                
                # If the sum of two adjacent numbers is less than the value of target, then we increase the counter by 1
                if nums[i] + nums[j] < target:
                    counter += 1

        return counter