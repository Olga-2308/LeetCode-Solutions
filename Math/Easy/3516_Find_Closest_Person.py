class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:

        # To determine the number of steps required by the first and second person, 
        # we need to find the absolute value of the difference between the first and third person and between the second and third. 
        # We take the absolute value because the movement can be in different directions, 
        # and we are only interested in the number of these steps.

        # If the number of steps of the first person is less than the second, then we return 1
        if abs(z-x) < abs(z-y):
            return 1
        
        # If the number of steps of the first person is greater than the second, then we return 2
        elif abs(z-x) > abs(z-y):
            return 2
        
        # otherwise, return 0. 
        # If the previous conditions are not met, then the number of steps is the same.
        else:
            return 0