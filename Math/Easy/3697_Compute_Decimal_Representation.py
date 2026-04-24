class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:

        components = []

        # We create a counter that will display the number of 0's required for each new digit of the number
        indx = 0

        # To work with each digit of a number, the number must be converted into a string
        num = str(n)

        # We create a loop in which we work with each digit of the number, starting from the end
        for i in range(len(num) - 1, -1, -1):

            # If the digit is 0, then the number is not added, but it is necessary to increase the counter, 
            # since there will be a transition to the next digit, where the number of 0 increases
            if num[i] == "0":
                indx += 1
            
            # If the number is greater than 0, then the number with 0 must be added to the list, which indicates the digit
            else:
                number = num[i] + "0" * indx
                components.append(int(number))
                indx += 1

        # sort the list as required in the problem statement.
        components.sort(reverse = True)

        return components