class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:

        counter = 0

        # Using a nested loop, we search for matching pairs of numbers
        for i in range(len(hours) - 1):
            for j in range(i+1, len(hours)):

                # A pair of numbers is suitable if the sum equals a full day, that is, 
                # the sum of the numbers is divisible by 24 without a remainder.
                if (hours[i] + hours[j]) % 24 == 0:
                    counter += 1

        return counter