class Solution:
    def isPathCrossing(self, path: str) -> bool:

        # We create a tuple to record coordinates and quickly search for matches
        points = {(0, 0)}

        # we determine the initial position
        UD = 0
        RL = 0

        # using a cycle, we take a step each time in accordance with the direction
        for char in path:
            if char == 'N':
                UD += 1
            elif char == 'S':
                UD -= 1
            elif char == 'E':
                RL += 1
            elif char == 'W':
                RL -= 1

            # after each step we determine new coordinates
            point = (UD,RL)

            # If the current point is in the tuple, 
            # it means we've already been here and immediately return true, 
            # otherwise we go to the end of the loop looking for matches 
            # and return false if the coordinates are not repeated.
            if point in points:
                return True
            else:
                # at each iteration we add coordinates to the tuple to search for possible further matches
                points.add(point)

        return False