class Solution:
    def findValidPair(self, s: str) -> str:

        d = {}
        number = str(s)

        # We create a loop in which we fill the dictionary
        for i in range(len(number)):

            # The key of an element is the character itself, and its value is the number of that character in the string.
            if number[i] not in d:
                d[number[i]] = 1
            else:
                d[number[i]] += 1

        # We create a loop in which we search for a pair of characters that satisfy the conditions of the problem
        for i in range(len(number) - 1):

            # We need two distinct adjacent string elements
            if number[i] != number[i+1]:

                # then we check if the number itself is equal to the number of times it appears in the string 
                # (the number of times a character appears in the dictionary value)
                if d[number[i]] == int(number[i]) and d[number[i+1]] == int(number[i+1]):

                    # Once we've found the first pair of characters, we return it in response
                    return number[i] + number[i+1]

        # If such a pair of characters is not found, then we return an empty string.
        return ""