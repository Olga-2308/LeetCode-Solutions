class Solution:
    def maxOperations(self, s: str) -> int:
        '''
        A 1 can move to the next 1 in one move, passing all the 0s between these two 1s in one go. 
        Therefore, we begin counting the number of 1s from left to right, 
        and increment the move counter only when we reach the boundary 0 (after which it goes back to 1). 
        When we reach 0, all the 1s found previously take another step. 
        After passing this 0, we then collect the 1s and move them all together through the 0s to the next 1.
        '''

        total = 0
        one = 0

        # We check each number in the array, we specify -1 since we are checking a pair of numbers (0 and 1)
        for i in range(len(s) - 1):

            # If we find 1, we increase the one counter by 1. 
            # This means that now each time this one will move until it reaches the end of the array.
            if s[i] == "1":
                one += 1

            # If we find a 0 followed by a 1, we need to shift all the 1s that were found previously. 
            # To do this, we increment the total counter by the number of previously found 1s.
            elif s[i] == "0" and s[i+1] == "1":
                total += one

        # Since the last character in the array isn't checked, it needs to be checked separately. 
        # If it's 0, all previously found 1s may be moved forward by another step, so we increment the overall counter.
        if s[-1] == "0":
            total += one

        return total