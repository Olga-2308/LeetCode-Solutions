class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        # We create counters to count vowels in strings 
        counter_a = 0
        counter_b = 0

        # create a string with vowels
        vowels = 'aeiouAEIOU'

        # find the middle of the line to divide the line into two equal parts
        middle = len(s) // 2

        # ''' we create new strings, where the first one is from the beginning of the given line to the middle, 
        # and the second one is from the middle to the end of the given line '''
        a = s[:middle]
        b = s[middle:]

        # We check each new line to see how many vowels it contains and increase the counter by 1 for each match.

        for char in a:
            if char in vowels:
                counter_a += 1
        
        for char in b:
            if char in vowels:
                counter_b += 1

        # If the number of vowels in the strings is the same, then return true, otherwise false
        if counter_a == counter_b:
            return True
        else:
            return False