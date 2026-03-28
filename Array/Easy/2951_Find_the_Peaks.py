class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:

        # create an empty list for the number indices
        peaks = []

        # create a loop in which we work with each number. 
        # begin the loop with the second number, index 1, since the leftmost number doesn't match the condition. 
        # We end the loop with the penultimate value. 

        # When we subtract one from the list length, this means we take the penultimate value in the list, 
        # compare it with the last one, and then end the loop (the loop doesn't go beyond the bounds).
        for i in range(1, len(mountain)-1):

            # if the number is greater than the previous and next values, then the condition is met
            if mountain[i] > mountain[i+1] and mountain[i] > mountain[i-1]:

                # add the index of a number to the list
                peaks.append(i)

        return peaks