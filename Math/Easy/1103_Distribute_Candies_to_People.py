class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:

        # we create an array whose length is equal to the number of people
        result = [0] * num_people
        candy = 1

        # the cycle continues until all the candies are distributed
        while candies > 0:
            for i in range(0, num_people):

                # If in the current iteration the number of candies 
                # we have to give away is less than the total remainder, 
                # then we give away the candies, subtract their quantities from the remainder, 
                # and increase the quantity for the next iteration by one.
                if candy < candies:
                    result[i] += candy
                    candies -= candy
                    candy += 1

                # If in the current iteration the number of candies 
                # we have to give away is less than or equal to the total remaining, 
                # then we give away the remaining candies and return the result, breaking the loop
                elif candy >= candies:
                    result[i] += candies
                    return result