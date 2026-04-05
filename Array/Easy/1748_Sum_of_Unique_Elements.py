class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:

        # create a variable in which we will count the sum of unique elements
        total = 0

        # create a loop in which we check each element in the list
        for num in nums:

            # If an element appears in the list once, it is unique and we add it to the general variable to calculate the sum.
            if nums.count(num) == 1:
                total += num

        return total