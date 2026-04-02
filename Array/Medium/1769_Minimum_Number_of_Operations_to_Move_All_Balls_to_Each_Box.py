class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        # create an empty list for the final result for each box
        result = []

        # create a nested loop in which we go through each box
        for i in range(len(boxes)):

            # create a variable to store all the steps from different boxes to the current one. 
            # reset the variable each time before counting the moves for a new box from the outer loop.
            total = 0
            
            # in the inner loop we check if there are balls inside the box that need to be moved
            for j in range(len(boxes)):

                # If the value is 1, then there is a ball in the box.
                if boxes[j] == '1':

                    # need to find the number of steps it takes for the ball to move from the inner loop box to the outer loop box. 
                    # need to find the absolute difference in the indices of the two boxes. This is the number of steps.
                    total += abs(j-i)
            
            # add the result to the current box of the outer loop
            result.append(total)

        return result