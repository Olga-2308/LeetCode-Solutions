class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        To get maximum profit, you need to buy shares at a lower price and sell them at a higher price.
        '''

        total = 0

        # Using a loop, we search for pairs of numbers whose purchase and sale will yield a positive number. 
        # Since we are checking pairs of numbers, we move the right boundary back one step.
        for i in range(len(prices) - 1):

            # If the first number is greater than or equal to the second, 
            # this means that we will not receive any profit from buying and selling, 
            # so we skip this pair and make the next one
            if prices[i] >= prices[i+1]:
                continue
            else:

                # If we make a profit after buying and selling a stock, 
                # then we find the difference in values ​​and add it to the overall result
                total += prices[i+1] - prices[i]

        return total