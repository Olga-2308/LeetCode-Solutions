class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:

        # Since according to the problem statement the given number will increase by 2 times each time, 
        # but it is necessary to sort the list in order to go through it not only once
        nums.sort()

        # create a loop in which we check each number, starting with the smallest one in the sorted array.
        for num in nums:

            # We start searching for a number equal to the given one. 
            # Once we find it, we double the variable and continue searching for the next one. 
            # Since the list is sorted, this number is either on the right side of the array or missing.
            if num == original:
                original = num * 2

        return original