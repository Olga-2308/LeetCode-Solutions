class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        # ''' We use the formula to find the number of odd numbers in a range: 
        # (high + 1) // 2 - the number of odd numbers in the range from 0 to high inclusive 
        # low // 2 - the number of odd numbers in the range from 0 to (low - 1) 
        # subtract the second from the first to find the number of odd numbers in a given range '''
        result = (high + 1) // 2 - low // 2
        
        return result


# class Solution:
    # def countOdds(self, low: int, high: int) -> int:
        # counter = 0
        # for num in range(low, high+1):
            # if num % 2 != 0:
                # counter += 1

        #return counter