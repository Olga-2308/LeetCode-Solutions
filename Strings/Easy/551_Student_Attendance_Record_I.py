class Solution:
    def checkRecord(self, s: str) -> bool:

        # create a counter to count the number of letters A in a string.
        counter = 0

        # create a loop in which we check each character in the string and count the number of letters A
        for char in s:
            if char == 'A':
                counter += 1

        # check whether two conditions of the problem are met simultaneously and return the corresponding result
        return counter < 2 and 'LLL' not in s