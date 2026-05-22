class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        # We create a dictionary that will store the number of banknotes of different denominations
        cash = {5:0, 10:0, 20:0}

        # If we were given 5, we don't need change and we just write the bill down in the dictionary.
        for num in bills:
            if num == 5:
                cash[5] += 1

            # If we were given a 10, we should give 5 as change. 
            # If 5 isn't in the dictionary, we return false. 
            # Otherwise, we remove the 5 note from the dictionary and add the 10 note.
            elif num == 10:
                if cash[5] <= 0:
                    return False
                else:
                    cash[5] -= 1
                    cash[10] += 1
                    
            # If we were given a 20-ruble note, we can get change back in two ways.
            elif num == 20:

                # The first priority is because it's the only way to get rid of the 1. 
                # You need one 10 and one 5 to give change and write 20 in the dictionary.
                if cash[10] > 0 and cash[5] > 0:
                    cash[10] -= 1
                    cash[5] -= 1
                    cash[20] += 1

                # If 10 is not in the dictionary, then we can give change from three 5s, 
                # if they are in the cash register
                elif cash[5] >= 3:
                    cash[5] -= 3
                    cash[20] += 1
                else:
                    return False

        return True