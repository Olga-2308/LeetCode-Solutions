class Solution:
    def isSameAfterReversals(self, num: int) -> bool:

        # the number for an even number of turns is equal to the original number if there is no 0 at the end

        # If the number is 0, then we return true, as specified in the problem statement.
        if num == 0:
            return True
        
        # If the number does not end in 0, then it will not change and we return true
        elif num % 10 != 0:
            return True
        
        # in all other cases the number will change and will be different from the original, so we return false
        else:
            return False 