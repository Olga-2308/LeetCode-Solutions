class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:

        # create an empty list for the missing numbers
        result = []

        # sort the list to determine the boundaries within which we need to look for the missing numbers.
        nums.sort()

        # create a loop in which we check each number. 
        # The loop runs from the beginning of the list to the end. 
        # Since the index starts with the minimum value in the list, we check whether this index is in the list. 
        # If the index is not there, we add it to the list, since this index is the missing number in the list.
        for i in range(min(nums), max(nums)):
            if i not in nums:
                result.append(i)

        return result