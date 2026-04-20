class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        '''
        We need to create a single array composed of two arrays according to certain rules. 
        First, we separate the numbers in the first array into two lists: those that appear in the second array and those that don't. 
        We sort the list of single elements according to the problem statement. 
        Then, we need to arrange the elements of the main array according to their positions in the second array.
        '''

        # Create empty lists to separate the numbers in the first array
        main = []
        remainder = []

        # We create a loop in which we check the numbers in the first array. 
        # If the number is in the second array, we add it to one list; if not, we add it to the other.
        for num in arr1:
            if num in arr2:
                main.append(num)
            else:
                remainder.append(num)

        # We sort an array of non-repeating numbers as required in the problem statement.
        remainder.sort()
        result = []

        # We create a loop in which we arrange the elements of the main loop in the correct order. 
        # To do this, we check whether each number is equal to the first element in the second array. 
        # After adding all matches, we remove the first element of the second array and continue checking.
        while len(arr2) != 0:
            for num in main:
                if num == arr2[0]:
                    result.append(num)
            del arr2[0]

        return result + remainder