class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:

        # create an empty list for the sums of numbers
        min_time = []

        # create a loop in which we work with each element (pair of numbers) in order
        for task in tasks:

            # find the sum of two values
            t = sum(task)

            # add the received amount to the list
            min_time.append(t)

        # return the minimum value from the list
        return min(min_time)