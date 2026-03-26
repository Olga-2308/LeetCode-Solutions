class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        # create an empty line in which we will enter the results
        result = []

        # find the element with the maximum number (value) of candies
        all_candies = max(candies)

        # create a loop in which we iterate over all the elements in order
        for i in range(len(candies)):

            # add the original value of candies to extraCandies
            total = candies[i] + extraCandies

            # If the obtained result is greater than or equal to the maximum found, then add True to the list, otherwise False
            if total >= all_candies:
                result.append(True)
            else:
                result.append(False)

        return result