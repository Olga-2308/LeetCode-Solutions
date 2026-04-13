class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # create an empty string into which we will add characters from the array of numbers
        number = ''

        # create an empty array to return the transformed array back to it
        result = []

        # create a loop in which we add each number in the array one by one to a string 
        # (before this, we convert each number into a string)
        for num in digits:
            number += str(num)

        # When we get one string of numbers, we need to add 1 to that number. 
        # To do this, we turn the string into a number and add 1.
        res = int(number) + 1

        # It needs to return an updated array of numbers. 
        # To do this, we create a loop in which we add each character of the string to the array one by one.
        for char in str(res):
            result.append(int(char))

        return result