class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        '''
        To find the maximum number, it is necessary to remove each occurrence of the given digit one by one 
        and determine the maximum number at each iteration using a function.
        '''

        max_num = 0

        # We check each character using a loop.
        for i in range(len(number)):

            # If the digit to be removed is found, create a new string from the slices 
            # that make up the original string, excluding the current digit.
            if number[i] == digit:
                new_num = number[:i] + number[i+1:]

                # convert the string to a number to find the maximum
                new_number = int(new_num)
                max_num = max(max_num, new_number)

        # returns the maximum number as a string
        return str(max_num)