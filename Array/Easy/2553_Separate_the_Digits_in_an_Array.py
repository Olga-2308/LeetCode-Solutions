class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:

        # create an empty list to add the results of the loop
        result = []

        # we create the first loop in which we work with each element
        for num in nums:

            # take an element and turn it into a string, because it is a string that can be split into individual characters
            s = str(num)

            # we create a nested loop in which we work with each separated character
            for char in s:

                # ''' add each character in order to the final list. 
                # Before doing this, we need to convert the character from a string back to an integer, as required in the condition. '''
                result.append(int(char))

        return result