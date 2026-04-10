class Solution:
    def divisorGame(self, n: int) -> bool:

        # Alice will always win if she is initially given an even number. 
        # She can always subtract the minimum divisor, 1, on her turn and return an odd number to Bob. 
        # Bob can also subtract 1 and return an even number to Alice, or subtract a divisor greater than 0. 
        # But any divisor will be odd. It turns out that when subtracting an odd divisor from an odd number, 
        # Alice will still get an even number, subtract 1 from it, and return an odd number to Bob again. 
        # And on her last turn, Alice will always win, returning 1 to Bob.

        return n % 2 == 0