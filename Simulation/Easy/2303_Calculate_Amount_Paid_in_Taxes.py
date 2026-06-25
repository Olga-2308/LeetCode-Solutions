class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:

        total = 0
        start = 0

        # We calculate the amount of taxes in each subarray using a loop.
        for i in range(len(brackets)):

            # To begin with, we determine the amount of money that will be subject to tax at the current rate.
            dollars = brackets[i][0] - start

            if dollars <= income:

                # If the current bracket range is within the remaining income, deduct it and calculate the tax.
                income -= dollars

                # Next, we will calculate the tax based on the current interest rate.
                tax = dollars / 100 * brackets[i][1]

                # We will add this amount to the total result.
                total += tax

            # If the resulting amount is equal to or less than the total sum, 
            # then this is the final amount we can tax. Once the tax amount is determined, 
            # we terminate the loop—since the funds are exhausted—and return the total tax amount.
            else:
                tax = income / 100 * brackets[i][1]
                total += tax
                break

            start = brackets[i][0]

        return total