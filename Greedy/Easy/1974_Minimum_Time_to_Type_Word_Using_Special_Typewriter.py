class Solution:
    def minTimeToType(self, word: str) -> int:

        total = 0

        # we find the length of the string, this value is also the time it takes to print each character
        color = len(word)

        # the beginning is on the first letter of the alphabet
        start = 'a'

        # Using a loop, we determine the distance between characters
        for i in range(len(word)):
            
            # To do this, we subtract the ordinal number of the current symbol in the loop 
            # from the ordinal number of the starting point
            one = abs(ord(start) - ord(word[i]))

            # We also calculate the second path, where the direction is counterclockwise. 
            # To find the distance, we need to subtract the distance of the first path from the total number of symbols.
            two = 26 - one

            # We add the minimum path to the general counter
            total += min(one, two)

            # update the initial position
            start = word[i]

        return total + color