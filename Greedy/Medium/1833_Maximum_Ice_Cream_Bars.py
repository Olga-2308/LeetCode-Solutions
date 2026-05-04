class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        '''
        To buy the maximum amount of ice cream, you need to buy them starting with the lowest price. 
        Therefore, you need to sort the array and increment the counter until the boy has enough money to buy ice cream.
        '''

        costs.sort()
        total = 0

        for cost in costs:

            # If there are more coins than the cost of the ice cream itself, 
            # then we subtract the cost of the ice cream and increase the counter by 1
            if cost <= coins:
                coins -= cost
                total += 1
 
        return total