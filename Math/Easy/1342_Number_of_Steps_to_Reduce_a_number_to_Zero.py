class Solution:
    def numberOfSteps(self, num: int) -> int:

        # Let's create a counter for counting steps
        counter = 0

        # we create a loop that runs until the number is greater than 0
        while num > 0:

            # check if the number is even
            if num % 2 == 0:
                # If the number is even, then we divide it by 2
                num = num // 2
                # add a step to the counter
                counter += 1

            elif num % 2 != 0:
                # If the number is odd, then subtract 1 from it
                num = num - 1
                # add a step to the counter
                counter += 1

        return counter
        