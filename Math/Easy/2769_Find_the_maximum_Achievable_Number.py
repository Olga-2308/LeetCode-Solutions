class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:

        # ''' num + 1 - the number increases by 1 in 1 move (by 2 units in 2 moves, etc.) 
        # --> therefore, it can be written as (num + t)
        # 
        # x - 1 - the number decreases by 1 in 1 move (by 2 units in 2 moves, etc.) 
        # --> therefore, it can be written as (x - t)
        # 
        # To find the value in which they will meet, the equality must be satisfied (num + t) = (x - t)
        # We derive the final formula:  (x = num + t + t --> x = num + 2t)'''

        x = t * 2 + num
        return x