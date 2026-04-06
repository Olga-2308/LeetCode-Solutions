class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        # create a list to which we will add the index numbers
        result = []

        # sort the list as specified in the problem statement
        nums.sort()

        # create a loop in which we check each number
        for i in range(len(nums)):

            # If the number is equal to the given one, then we add the index of this number to the list
            if nums[i] == target:
                result.append(i)

        return result