class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        
        # we determine the number of cells on the deck
        cells = n * n

        # There can be two situations: 
        # the first is when there is enough space on deck, 
        # and the second is when there is not enough space

        # If all cells are filled with containers and their weight does not exceed the maximum, 
        # then we return the total number of cells
        if cells * w <= maxWeight:
            return cells
        
        # If, when filling all the cells on the deck, the maximum weight was exceeded, 
        # then it is necessary to determine how many containers 
        # we can leave on the deck so that their weight does not exceed the maximum
        else:
            return maxWeight // w