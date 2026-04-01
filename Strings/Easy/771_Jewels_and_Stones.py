class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        # create a counter for counting jewels among stones
        counter = 0

        # create a loop in which we check each stone.
        for stone in stones:

            # If the symbol is among the stones in the line of jewelry, then we increase the counter by 1
            if stone in jewels:
                counter += 1

        return counter