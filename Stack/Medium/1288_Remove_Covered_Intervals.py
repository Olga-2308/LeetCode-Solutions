class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        # sort the intervals so that each subsequent left boundary of the interval 
        # is greater than or equal to the previous one
        intervals.sort()

        # If necessary, we add an interval to the array one by one, 
        # which becomes the main one during the comparison
        stack = []

        for num in intervals:

            # we start with the first interval, which is added to the stack
            if not stack:
                stack.append(num)

            # Now each subsequent interval in the loop is compared with the last interval of the stack, 
            # since it is guaranteed to have the largest right and left boundaries 
            # (otherwise, one of the intervals must be absorbed by the other)
            else:

                # if the boundaries of the current interval from the loop are inside the boundaries of the interval 
                # from the stack, then the current interval from the loop will be covered by the interval from the stack, 
                # and therefore the current iteration can be skipped
                if stack[-1][0] <= num[0] and stack[-1][1] >= num[1]:
                    continue

                # If the boundaries of the current interval from the stack are inside the boundaries of the interval from the loop, 
                # then the last interval from the stack will be covered by the interval from the loop, 
                # and therefore we remove the last element of the stack and add a new interval in its place, 
                # which will subsequently determine the new boundaries on both sides
                elif stack[-1][0] >= num[0] and stack[-1][1] <= num[1]:
                    del stack[-1]
                    stack.append(num)

                # If coverage does not occur, this means the intervals intersect or, conversely, are far apart. 
                # In either case, the interval is added to the stack to update the correct boundaries.
                else:
                    stack.append(num)

        # We return the stack length, which shows how much interval remains after all overlaps.
        return len(stack)