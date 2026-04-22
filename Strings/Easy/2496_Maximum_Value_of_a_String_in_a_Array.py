class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        '''
        We need to return the maximum value among numbers. 
        We create numbers as follows: if the string consists only of numbers, then the value of the number is the number.
        If the string contains letters, then the length of the string is the number.
        '''

        result = []

        for word in strs:

            # If the string consists of numbers, then we convert the string into a number and add the result to the list
            if word .isdigit():
                result.append(int(word))
            
            # Otherwise, there are letters in the string, and then we add the length of the string to the list.
            else:
                result.append(len(word))

        # return the maximum value as specified in the problem statement.
        return max(result)