class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        # we define the boundaries of the search
        left = 0
        right = len(arr) - 1

        # we run the loop until the array boundaries converge to a single value
        while left < right:

            # find the middle of the current array
            mid = (left + right) // 2

            # If the number of the array under the central index is less than the number to the right of it, 
            # this means that the peak is still ahead (on the right side), and there is definitely nothing on the left side
            if arr[mid] < arr[mid+1]:

                # we remove the entire left part, including the current element, and define a new left boundary, 
                # which is equal to the next element after the central one (the central one is not needed, 
                # since we just checked it and it is smaller than the next one, so from it)
                left = mid + 1

            # If the central element is larger than the next one (to the right), 
            # it means the elements to the right are decreasing and there's no peak there. 
            # We need to continue checking the numbers on the left side, 
            # and the numbers on the right side are no longer needed, 
            # so we remove the right side and update the right boundary. 
            # It's now at the current central value. We use this boundary because the current center could also be a peak.
            else:
                right = mid

        return left