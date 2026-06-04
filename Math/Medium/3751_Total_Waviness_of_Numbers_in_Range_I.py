class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        counter = 0

        # we create an array of numbers in which we will search for points
        for i in range(num1, num2 + 1):
            number = str(i)

            # If the number is two-digit, then it has no peaks and we skip it
            if len(number) <= 2:
                continue

            # in a nested loop we check each character (digit) of the string (number) and count each peak that we find
            for j in range(1, len(number) - 1):
                if number[j] > number[j-1] and number[j] > number[j+1]:
                    counter += 1
                elif number[j] < number[j-1] and number[j] < number[j+1]:
                    counter += 1

        return counter