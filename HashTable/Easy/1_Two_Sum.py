class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = {}

        for i in range(len(nums)):

            # We create a loop in which we search for a pair of matching numbers. 
            # The first number is the current number in the loop, and the second number is found using a formula. 
            # At the current iteration, we have the first number in the loop; to find the second, we need to check the dictionary.
            num = target - nums[i]

            # If the second missing number is found in the dictionary, 
            # then we return the indices of the current number in the loop and the value (index) from the dictionary
            if num in n:
                return [n[num], i]
            
            # If the pair of numbers is not found, then we write a new number-index pair into the dictionary
            else:
                n[nums[i]] = i