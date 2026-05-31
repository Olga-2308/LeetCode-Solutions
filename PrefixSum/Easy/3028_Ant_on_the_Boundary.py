class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        '''
        The boundary is determined when the ant moves in one direction; 
        as soon as its direction changes, we can record the boundary. 
        To determine whether it has reached this boundary again, we need to track its return movement. 
        The moment of reaching the boundary is determined by the equality of steps (the absolute distance).
        '''

        # we define the boundary as 0
        left = 0
        right = 0
        counter = 0

        
        for num in nums:
            # If the number is greater than 0, then the ant is moving to the right and we increase the corresponding limit; 
            # if the number is negative, then the movement is directed to the left.
            if num > 0:
                right += num
            else:
                left -= num

            # if the values ​​of the boundaries are equal, this means that at the moment, 
            # the ant was on the boundary, then began to move to another boundary 
            # and after that returned to the initial point
            if abs(left) == right:
                counter += 1

        return counter

        '''
        position = 0
        counter = 0
        
        for num in nums:
            position += num
            if position == 0:
                counter += 1
                
        return counter
        '''