class Solution:
    def clearDigits(self, s: str) -> str:

        # create an empty list for the final result
        res = []

        # create a loop in which we check each character in order
        for char in s:
            
            # If the character being checked is a digit, it is skipped in the list.
            if char.isdigit():

                # And according to the condition, the character to the left of the number must also be removed. 
                # If the list already contains some letters, then the last letter from the list is removed.
                if res:
                    res.pop()
            
            # If the symbol is a letter, then we add it to the list
            else: 
                res.append(char)

        # After we have received the final list, it must be converted back into a string, as required in the problem statement
        result = ''.join(res)

        return result