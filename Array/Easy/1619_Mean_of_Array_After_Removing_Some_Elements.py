class Solution:
    def trimMean(self, arr: List[int]) -> float:

        # We find the number of elements that will be included in the 5% 
        # that need to be removed from both ends of the array.
        part = int(len(arr) / 100 * 5)

        # sort the array to determine the minimum and maximum elements of the array
        arr.sort()

        # define a new array using a slice that removes elements from both ends of the original array
        new_arr = arr[part:-part]

        # we determine the arithmetic mean using the formula
        average = sum(new_arr) / len(new_arr)

        return average