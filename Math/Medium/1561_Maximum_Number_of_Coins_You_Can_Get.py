class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        # To collect the maximum number of coins, Bob needs to collect the smallest coins. 
        # To find them, we sort the array.
        piles.sort()

        # Since the number of piles is a multiple of 3, each of us will get an equal number of piles. 
        # So, Bob will have the smallest third.
        part = len(piles) // 3

        # Using the cutter, we form the remaining two largest parts of the momnet, 
        # which need to be divided between me and Alice.
        my_and_Alice_part = piles[part:]
        my_coins = 0

        # I take each middle value from the triplet, and Alice takes the largest one. 
        # This means that in the remaining array of numbers from each pair, 
        # Alice takes the largest number, and I take the next largest.
        for i in range(0, len(my_and_Alice_part), 2):
            my_coins += my_and_Alice_part[i]

        return my_coins