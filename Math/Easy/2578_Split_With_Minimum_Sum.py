class Solution:
    def splitNum(self, num: int) -> int:
        
        # To obtain the minimum sum from the original number, 
        # you need to create two numbers that are as small and as close in value as possible. 
        # To do this, you need to create two numbers with the minimum digits in the highest digits 
        # and distribute them alternately among the two numbers.

        # We create an array of digits from a number. 
        # To get a list, we convert the number to a string.
        number = list(str(num))

        # sort the list in ascending order to make it easier to distribute the numbers into new numbers
        number.sort()

        # create empty lists for new numbers
        first = []
        second = []

        # we create a loop in which we create new numbers
        for i in range(len(number)):

            # One way to distribute the digits of a number alternately into two lists is to check the parity of the index. 
            # Since it alternates every other index, the numbers will also be evenly distributed across the lists.
            if i % 2 == 0:
                second.append(number[i])

            # If the index of a number is even, then we add the digit to one list; if it is odd, then to another.
            else:
                first.append(number[i])

        # After we have received two lists with new digits from the number, 
        # we need to convert them into strings to change the data type to a number and find the sum
        f = ''.join(first)
        s = ''.join(second)

        # we return the sum of the received numbers
        return int(s) + int(f)