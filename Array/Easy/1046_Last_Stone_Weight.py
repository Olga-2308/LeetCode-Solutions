class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        During the game, you must destroy all the stones or return the value of the last one. 
        You must sort the array in descending order and alternately take pairs of numbers 
        and reduce the array elements according to the rules of the game.
        '''

        # We create a cycle that runs until the last stone remains.
        while len(stones) > 1:

            # We sort the array to make it easier to take adjacent values
            stones.sort(reverse = True)

            # If the first two maximum values ​​are equal, they are destroyed 
            # (elements are removed from the array)
            if stones[0] == stones[1]:
                del stones[1]
                del stones[0]
            
            # If the two maximum values ​​are not equal, then we leave only one stone equal to the difference between the two values.
            elif stones[0] != stones[1]:
                stones[0] = stones[0] - stones[1]
                del stones[1]

        # If there are no stones left, return 0, otherwise the value of the remaining element
        if len(stones) == 0:
            return 0
        elif len(stones) == 1:
            return stones[0]