class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:

        good = []

        # We check each restaurant using a loop
        for i in range(len(restaurants)):

            # we define metrics
            vegan = restaurants[i][2]
            price = restaurants[i][3]
            dist = restaurants[i][4]

            # If the value is 0, this means that this metric is not checked and all restaurants are suitable.
            if veganFriendly == 0:

                # We check restaurants by price and distance and add suitable ones to the list
                if price <= maxPrice and dist <= maxDistance:
                    good.append([restaurants[i][1], restaurants[i][0]])

            # If the value is 1, it means that restaurants that are vegan-friendly are suitable (value is 1)
            elif veganFriendly == 1: 
                if vegan == veganFriendly and price <= maxPrice and dist <= maxDistance:
                    good.append([restaurants[i][1], restaurants[i][0]])

        # We sort the array, since the pair of values ​​for each restaurant was added in the form (rating - id), 
        # then the restaurants will first be sorted by rating, and if the rating is the same, 
        # then the distribution will be from larger to smaller by the second element of the subarray
        good.sort(reverse = True)
        result = []

        # We create and return a list of restaurants sorted by rating.
        for i in range(len(good)):
            result.append(good[i][1])

        return result