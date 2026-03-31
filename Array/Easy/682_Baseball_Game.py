class Solution:
    def calPoints(self, operations: List[str]) -> int:

        # create an empty list to record the results
        result = []

        # create a loop to check each line in the list
        for s in operations:

            # if the symbol is +, then we add the last two values ​​from the list of results
            if s == '+':
                result.append(result[-1] + result[-2])

            # If the symbol is equal to D, then we increase the last value in the list of results by 2 times
            elif s == 'D':
                result.append(result[-1] * 2)

            # If the symbol is equal to C, then remove the last element from the result list.
            elif s == 'C':
                result.pop(-1)

            # If the symbol is not one of those above, then we add this symbol in numeric format to the results list 
            # (when using the .isdigit() method, negative numbers don't pass, 
            # so we just add the numbers at the end since they don't match the characters above)
            else:
                result.append(int(s))

        # return the sum of the result
        return sum(result)