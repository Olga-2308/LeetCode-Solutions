class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        # create a counter to count mismatches
        counter = 0

        # create a new copy of the list
        expected = heights[:]
        # sort the new list in ascending order
        expected.sort()

        # create a loop in which we compare all the elements from the two lists in order.
        for i in range(len(heights)):

            # if the elements do not match, the counter increases by 1
            if heights[i] != expected[i]:
                counter += 1

        return counter