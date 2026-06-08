class Solution:
    def dayOfYear(self, date: str) -> int:

        # We turn the string into an array of strings so that we can work with each value separately.
        numbers = date.split('-')
        result = 0

        # we determine the numerical values ​​of the year, month, and number of days
        year = int(numbers[0])
        month = int(numbers[1])
        days = int(numbers[2])

        # If the month is 1, then we simply return the current number of days
        if month == 1:
            return days
        total_days = 31

        # When calculating each subsequent month, 
        # you must add all the days of the previous month
        if month == 2:
            result = total_days + days
        total_days += 28

        if month == 3:
            result = total_days + days
        total_days += 31
    
        if month == 4:
            result = total_days + days
        total_days += 30

        if month == 5:
            result = total_days + days
        total_days += 31

        if month == 6:
            result = total_days + days
        total_days += 30

        if month == 7:
            result = total_days + days
        total_days += 31

        if month == 8:
            result = total_days + days
        total_days += 31

        if month == 9:
            result = total_days + days
        total_days += 30

        if month == 10:
            result = total_days + days
        total_days += 31

        if month == 11:
            result = total_days + days
        total_days += 30

        if month == 12:
            result = total_days + days

        # We determine whether it is a leap year or not. If it is, we add 1 to the result 
        # (we only start checking if there are more than 2 months, otherwise an extra 1 will be added, 
        # since February may not be a full month according to the problem statement).
        if month > 2:
            if year % 400 == 0:
                return result + 1
            elif year % 4 == 0 and year % 100 != 0:
                return result + 1
      
        return result