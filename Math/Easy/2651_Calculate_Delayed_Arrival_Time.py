class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:

        # To determine the arrival time, you need to add the delay time to the current time
        time = arrivalTime + delayedTime

        # If the new arrival time is within 24 hours, then we return the current result
        if time < 24:
            return time
        
        # If the result exceeds the daily limit, then it is necessary to determine what time the arrival will be in the following days
        else:
            return time - 24
        
        # The solution can also be written in one line:

        # result = (arrivalTime + delayedTime) % 24

        # The remainder of the division will always show the arrival time; 
        # if the result is less than 24 hours, it will be 0 integers and the desired arrival time; 
        # if it is more than 24 hours, 
        # the remainder of the division will skip 1 (one day) and show the remainder of the new day, 
        # which is the arrival time.