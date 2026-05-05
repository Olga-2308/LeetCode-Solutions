class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:

        place = []

        # We determine at what places (indices) the required numbers are located in the array 
        # (the number is suitable if it is equal to the given x)
        for i in range(len(nums)):
            if nums[i] == x:
                place.append(i)

        result = []

        # Next, you need to check each request and return the location of a specific number.
        for q in queries:

            # If the serial number of the number occurrence is greater than the length of the array where all the indices are stored, 
            # then we return -1, since such a number simply does not exist and the query cannot be executed
            if q > len(place):
                result.append(-1)

            # If such a number exists, its index must be returned. Since we need to return the index, 
            # and the numbers in the created array are written under an ordinal number, 
            # we must subtract 1 to return the index.
            else:
                result.append(place[q - 1])

        return result