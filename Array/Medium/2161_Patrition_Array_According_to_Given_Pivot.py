class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        # create empty lists to divide numbers based on the conditions of the problem.
        less = []
        p = []
        more = []

        # create a loop in which we compare each number in order
        for i in range(len(nums)):

            # If the number is less than the specified one, then we add this number to the list of less
            if nums[i] < pivot:
                less.append(nums[i])

            # If the number is equal to the given one, then we add this number to the list p
            elif nums[i] == pivot:
                p.append(nums[i])

            # otherwise we add the number to the list more
            else: 
                more.append(nums[i])

        # concatenate the lists and return the result
        result = less + p + more

        return result