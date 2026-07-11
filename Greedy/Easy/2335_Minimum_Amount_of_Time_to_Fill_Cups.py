class Solution:
    def fillCups(self, amount: List[int]) -> int:
        '''
        To get the minimum number of minutes, you need to fill the cup completely with both types of water each time, 
        starting with the largest amount for more even distribution. Then add the remainder in one of the types.
        '''

        counter = 0

        # we draw water until at least one of the dispensers is empty (the sum of the numbers is greater than 0)
        while sum(amount) > 0:

            # We sort the array in descending order so that we take water from the largest dispenser each time. 
            # This will ensure an even distribution of water and allow us to create 
            # as many pairs of positive numbers as possible.
            amount.sort(reverse = True)

            # If the second element is 0, 
            # this means that there is water left only in the first dispenser and to collect it all, 
            # it is necessary to spend a unit of time for each unit of water, 
            # so we add the entire remainder to the total counter
            if amount[1] == 0:
                counter += amount[0]  
                break  

            # If there is water in two or more dispensers, this means that in one unit of time we can take two units of water
            amount[0] -= 1
            amount[1] -= 1
            counter += 1

        return counter