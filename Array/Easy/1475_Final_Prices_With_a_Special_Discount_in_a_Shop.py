class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        # create a copy of the list with prices to update the values
        result = prices[:]

        # create a nested loop in which we compare prices with each other.
        for i in range(len(prices)):

            # shift the second cycle by 1 step to avoid repeating identical numbers and to avoid comparing the number with itself
            for j in range(i+1, len(prices)):

                # If the current price is greater than or equal to the value on the right, 
                # then we subtract the found price of the smaller value from the current price
                if prices[i] >= prices[j]:

                    # find a new price
                    new_pr = prices[i] - prices[j]

                    # updating the price in the list
                    result[i] = new_pr

                    # As soon as the price is changed, we stop the internal cycle
                    break

        return result