class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        # We create a dictionary and a list for numbers that are not in the sample array.
        d = {}
        remainders = []

        # converting a sample array into a set for faster searching
        arr = set(arr2)

        for num in arr1:

            # Using a loop, we check all the numbers in the array that needs to be converted. 
            # If the number isn't in the sample, we add it to the list of remainders.
            if num not in arr:
                remainders.append(num)

            # If the number is in the sample, then we write the frequencies of all numbers in the dictionary
            else:
                if num not in d:
                    d[num] = 1
                else:
                    d[num] += 1

        # We create an array in which we will distribute the numbers in the correct order.
        main = []

        # We sort the remainders as they need to be returned at the end in ascending order.
        remainders.sort()

        # we fill the main array, in which we add the number as many times as the frequency in the array that it has
        for num in arr2:
            main.extend([num] * d[num])

        return main + remainders