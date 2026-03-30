class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:

# To calculate the minimum number of moves required to solve the problem, 
# you need to sort the two lists and count the number of moves in pairs

        # create a counter to count the number of moves
        counter = 0

        # sorting lists
        seats.sort()
        students.sort()

        # create a loop in which we work with each pair of numbers
        for i in range(len(seats)):

            # If the numbers are not equal, then moves are required to equalize them. 
            # We find the absolute value of the difference between the numbers—this is the required number of moves.
            if seats[i] != students[i]:

                # add these steps to the general counter
                moves = abs(seats[i] - students[i])
                counter += moves

        return counter
        