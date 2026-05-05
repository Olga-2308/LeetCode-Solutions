class Solution:
    def removeDuplicates(self, s: str) -> str:

        # we create an empty array where we will add characters from the string one by one
        ss = []

        # We check each character using a loop
        for char in s:

            # each time we add a character to the array
            ss.append(char)

            # and if there are at least two characters in the array, 
            # then each time after adding it is necessary 
            # to check whether the last two elements form a pair with the same characters
            if len(ss) >= 2 and ss[-1] == ss[-2]:

                # We delete the last two elements from the array one by one. 
                # -1 and -1 are specified because when the last character is deleted, 
                # the indexing shifts and the penultimate element (-2) becomes the last one (-1) after the last one is deleted.
                del ss[-1]
                del ss[-1]

        # we return the string, which is required in the problem statement
        return "".join(ss)