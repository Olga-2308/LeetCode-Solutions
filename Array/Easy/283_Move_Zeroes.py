class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # create empty arrays for zeros and other digits to create an array of numbers in the correct order.
        digits = []
        zero = []

        # create a loop in which we sort the numbers into the corresponding arrays.
        for num in nums:
            if num == 0:
                zero.append(num)
            else:
                digits.append(num)

        # update the original list in place, adding first numbers and then zeros according to the problem statement
        nums[:] = digits + zero