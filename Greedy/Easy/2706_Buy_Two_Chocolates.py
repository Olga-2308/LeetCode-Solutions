class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:

        # We sort the array to quickly find two chocolate bars at the lowest price.
        prices.sort()

        # We find the cost of the two least expensive chocolate bars.
        buy = prices[0] + prices[1]

        # If we need more money to make a purchase than we have, 
        # we cannot buy chocolates and then we return the amount of money that we had initially
        if buy > money:
            return money
        
        # If there is enough money, then we determine the amount of money remaining and return it
        else:
            return money - buy