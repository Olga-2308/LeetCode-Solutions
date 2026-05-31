class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:

        counter = 0

        # Using a triple loop, we check whether it is possible to distribute all the candies among the children; 
        # the limit of the loop is the maximum number of candies allowed
        for i in range(n + 1):
            for j in range(n + 1):
                for k in range(n + 1):

                    # If all the candies are distributed among three children 
                    # (the sum of the three numbers is equal to the total number of candies) 
                    # and the number of candies for each child does not exceed the limit, 
                    # then we increase the counter
                    if (i + j + k) == n and i <= limit and j <= limit and k <= limit:
                        counter += 1

        return counter