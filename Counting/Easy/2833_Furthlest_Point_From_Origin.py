class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:

        # count the number of each character in a string
        left = moves.count("L")
        right = moves.count("R")
        add = moves.count("_")

        # When moving to the right, we'll move into positive numbers, and when moving to the left, into negative numbers. 
        # Therefore, to find the maximum distance from a point to two possible endpoints, 
        # we need to find the absolute value of the difference.
        return abs(left - right) + add