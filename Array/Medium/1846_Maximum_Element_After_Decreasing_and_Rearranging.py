class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        # we sort the array, since the final sequence should be from smallest to largest
        arr.sort()

        # the first element of an array must always be one
        arr[0] = 1
        
        # using a loop we check whether the difference between two adjacent numbers is greater than 1, 
        # and if the difference is greater than 1, then we decrease the current element
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] > 1:
                arr[i] = arr[i-1] + 1
                
        return arr[-1]