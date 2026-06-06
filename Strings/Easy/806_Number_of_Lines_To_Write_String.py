class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:

        # We create a variable to count lines, 
        # so that at least one line will always be filled with a certain number of characters, 
        # then we set the value to 1
        lines = 1

        # We create a variable to calculate the width to determine when the overflow occurs.
        last_width = 0

        for char in s:

            # We write characters one by one into a string and determine the width of each character in the string 
            # (we determine the ordinal number of the character and find its width in the array)
            total = widths[ord(char) - 97]
            
            # If, when writing this character on the current line, the width does not exceed 100 pixels, 
            # then the character is written and its width is added to the total width of the line
            if last_width + total <= 100:
                last_width += total

            # If a character goes beyond the limit, we move to a new line 
            # (increment the line counter) and update the total line width value, 
            # where the current length becomes equal to the width of the first character in the new line.
            else:
                lines += 1
                last_width = total  

        return [lines, last_width]