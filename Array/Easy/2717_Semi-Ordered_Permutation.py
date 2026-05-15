class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        '''
        To determine the minimum number of operations needed to return the numbers to their places, 
        it is necessary to determine the distance between the beginning and the corresponding number 
        and the end and the corresponding number
        '''

        # the array starts from 1 and the maximum number is defined as the length of the array
        m = 1
        n = len(nums)

        total = 0

        # If the numbers are in their places, then we return 0, 
        # since no permutations are needed
        if nums[0] == m and nums[-1] == n:
            return 0

        # using a loop we find the locations of numbers
        for i in range(len(nums)):

            # Once we find 1, we determine how many operations need to be performed to return it to the first position. 
            # The index shows the number of operations.
            if nums[i] == m:
                total += i
                start = i

            # Once the last number has been found, it's necessary to determine how many permutations are required to return it to the end. 
            # To do this, subtract the current index from the array length. However, 
            # since indexing starts at 0 and the count starts at 1, we add 1 to the index to get the exact number of permutations.
            elif nums[i] == n:
                total += n - (i + 1)
                end = i

        # If the numbers intersect during the movements, 
        # then two numbers are moved simultaneously during one permutation, 
        # therefore, one extra step must be removed from the overall result
        if start < end:
            return total
        else:
            return total - 1