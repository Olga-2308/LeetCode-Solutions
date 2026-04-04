class Solution:
    def totalMoney(self, n: int) -> int:

        # create a variable to count the total amount of money
        total = 0

        # We create a cycle in which we count the amount of money set aside for the current day
        for i in range(n):

            # by how much does the amount of money increase this week?
            week = i // 7

            # How much money is set aside on the current day?
            day = i % 7

            # We find the total amount of money per day and add one. 
            # This is necessary because the index starts at 0, and the daily coins start at 1. 
            # And this difference of 1 is compensated daily.
            total += (week + day) + 1

        return total
    
# Let's look at this version of the code using the example of counting money over the course of two weeks.

# Let's imagine that we have two cash flows that give a certain amount of money every day.

# First flow: week is the amount of money given out over the course of 1 week. 
# The problem statement states that: 
    # 0 units for the week 1; 
    # +1 unit for week 2; 
    # +2 units for week 3.

# Second flow: day - this is the amount of money that is issued during the week. 
# This is a fixed number for each day of the week, namely: 1 2 3 4 5 6 7 units respectively. 

# Let's calculate weeks 1 and 2:
 
    # 1 week:
 # WEEK:   0   0   0   0   0   0   0   
  # DAY:   1   2   3   4   5   6   7   -->     1   2   3   4   5   6   7 (28 units will be in the bank after the first week)
 
    # 2 week
 # WEEK:   1   1   1   1   1   1   1
  # DAY:   1   2   3   4   5   6   7   -->     2   3   4   5   6   7   8 (35 units will be in the bank after the second week)
 
# It turns out that after two weeks of daily deposits, the bank will have 63 units.
 
# To transfer this logic into code, you also need to create two variables that will simultaneously show the amount of money set aside for the current day.
 
# The WEEK flow remains unchanged for 7 days and increases by 1 after the transition to the eighth day.
# This movement of numbers is realized through integer division, where the result of this division will show exactly how much money will be put into the bank.
    
    # i // 7 = 0 (This result will be from day 1 to day 7)
    # i // 7 = 1 (from day 8 to day 14)
    # i // 7 = 2 (from 5 to 21 days)
 
# Flow DAY increases the amount of money by 1 daily. 
# Such an increase can be realized when searching for the remainder of a division:
    # i(0) % 7 = 0 (1 day)
    # i(1) % 7 = 1
    # i(2) % 7 = 2
    # i(3) % 7 = 3
    # i(4) % 7 = 4
    # i(5) % 7 = 5
    # i(6) % 7 = 6

    # i(7) % 7 = 0 (8 day)
 
# Since the index in the cycle starts from 0, then during the week one unit is missing (7 units per week, 14 units in 2 weeks, etc.)
# That's why 1 is added to the total
# The loop continues until all the days specified in the problem statement are counted.