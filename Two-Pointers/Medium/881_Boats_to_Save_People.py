class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''
        To use as few boats as possible, it's best to only seat two people per boat. 
        A boat is more likely to accommodate one person of maximum weight and one of minimum weight, 
        if the limit allows; otherwise, one person will occupy one boat.
        '''

        boats = 0

        # We determine the beginning of the pointers, 
        # where one will go from the smallest numbers, the second - from the largest
        i = 0
        j = len(people) - 1

        # We sort the array so that the numbers are in order from minimum to maximum, 
        # to make it easier for people to board the boat.
        people.sort()


        while i <= j:

            # If two people can fit in one boat and they don't exceed the limit, 
            # then we take one boat and move each pointer one step toward the center.
            if people[i] + people[j] <= limit:
                boats += 1
                i += 1
                j -= 1

            # If the limit is exceeded, then we take one boat and put a heavier person in it, 
            # and move the indicator to the next person
            else:
                boats += 1
                j -= 1

        return boats