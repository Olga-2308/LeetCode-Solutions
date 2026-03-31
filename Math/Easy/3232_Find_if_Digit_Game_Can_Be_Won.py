class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:

        # create lists for numbers with one digit and two digits
        single_digit = []
        double_digit = []

        # we create a loop in which we iterate over each number from the list
        for num in nums:

            # We convert the number into a string and count the number of characters. 
            # If the string contains one character, then the number consists of one digit. 
            # We convert the string back to a number and add it to the corresponding list.
            if len(str(num)) == 1:
                single_digit.append(num)

            # otherwise we add the number to the second list
            else:
                double_digit.append(num)

        # For Alice to win, the sum of her numbers must exceed the sum of Bob's numbers. 
        # Alice can win if the sum of the first list is strictly greater than the second, or vice versa. 
        # But Alice won't win if the sums of the numbers are the same. Based on this, we formulate the condition:
        if sum(single_digit) != sum(double_digit):
            return True
        else:
            return False