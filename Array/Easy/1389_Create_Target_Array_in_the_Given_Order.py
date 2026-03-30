class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        # create an empty list to write the numbers in the correct order
        result = []

        # create a loop in which we work with each element in order
        for i in range(len(nums)):

            # Using the insert method, we replace an element in the list 
            # (we name the list we need - we specify the insert method -> 
            # we specify the element to be replaced -> 
            # we specify the element that will be written instead of the selected one)
            result.insert(index[i], nums[i])
            
        return result