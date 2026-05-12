class Solution:
    def convertTime(self, current: str, correct: str) -> int:

        # We transform strings into an array of strings: which consist of numbers
        nums_current = current.split(":")
        nums_correct = correct.split(":")

        # convert the current time into minutes
        cur_h = int(nums_current[0]) * 60
        cur_min = int(nums_current[1]) 
        total_current = cur_h + cur_min

        # convert the correct time into minutes
        cor_h = int(nums_correct[0]) * 60
        cor_min = int(nums_correct[1]) 
        total_correct = cor_h + cor_min

        # find the difference between the times in minutes
        diff = total_correct - total_current
        counter = 0

        # Each time we subtract the maximum values ​​from the difference and count the number of steps, 
        # the cycle runs until the minutes run out
        while diff > 0:
            if diff >= 60:
                diff -= 60
                counter += 1
            elif diff >= 15:
                diff -= 15
                counter += 1
            elif diff >= 5:
                diff -= 5
                counter += 1
            elif diff >= 1:
                diff -= 1
                counter += 1

        return counter