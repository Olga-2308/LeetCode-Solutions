class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        # create a variable to calculate the result of arithmetic operations
        counter = 0

        # Using a loop, we iterate through each string in the list
        for char in operations:

            # If the symbol is "++X'" or "X++", then add 1
            if char == '++X' or char == 'X++':
                counter += 1

            # otherwise we subtract one    
            else:
                counter -= 1

        return counter