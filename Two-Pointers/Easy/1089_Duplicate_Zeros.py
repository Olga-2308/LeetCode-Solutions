class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        i = 0

        # Using a loop, we duplicate the zeros in the array in one pass 
        # and remove the last element to preserve the array length.
        while i < len(arr) - 1:

            # If the number is not 0, then we skip it and move one step to the right
            if arr[i] != 0:
                i += 1
            
            # If the number is 0, we duplicate it, 
            # move two steps to the right to skip the new zero in the array, 
            # and delete the last element.
            elif arr[i] == 0:
                arr.insert(i + 1, arr[i])
                i += 2
                del arr[-1]