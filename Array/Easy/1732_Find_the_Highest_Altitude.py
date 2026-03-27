class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        # create an empty list where we will add new points
        # put 0 at the beginning of the list, since this is the starting point
        new_gain = [0]

        # create a variable with a zero value from which the movement begins
        point = 0

        # we create a loop in which the value under the corresponding index is added to each previous value
        for i in range(len(gain)):
            point += gain[i]

            # add the received value to the list
            new_gain.append(point)

        # we find the maximum value among the new heights
        result = max(new_gain)

        return result