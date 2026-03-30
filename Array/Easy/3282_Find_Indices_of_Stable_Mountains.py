class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:

        # create an empty list for the appropriate indices
        result = []

        # We create a loop in which we work with each element. 
        # According to the problem statement, we need to specify the index of the mountain whose previous mountain is higher than threshold. 
        # Therefore, we start with the first element and, if the condition is met, write the index of the second mountain to the result. 
        # We must subtract 1 from the list length to avoid exceeding the index bounds. 
        # In the final iteration, we need to take the penultimate element of the list and compare it. 
        # If the condition is met, then the index of the last element is written to the result. And this is where the loop ends.
        for i in range(len(height)-1):

            # if the current value is strictly greater than threshold
            if height[i] > threshold:

                # then we add the index of the next mountain to the list
                result.append(i+1)

        return result