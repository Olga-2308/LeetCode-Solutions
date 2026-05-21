class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:

        total = 0
        d = {}

        # we count the number of each task
        for task in tasks:
            if task not in d:
                d[task] = 1
            else:
                d[task] += 1

        
        for freq in d.values():

            # If the task occurs once, then it cannot be completed and we return -1
            if freq == 1:
                return -1
            
            # If the frequency is divisible by 3, 
            # then all tasks can be closed using the maximum capability.
            if freq % 3 == 0:
                total += freq // 3

            # If it's not divisible, then the remainder must be taken into account; we take all tasks by the maximum number. 
            # The remainder will be either 1 or 2, which can be closed in one additional step.
            else:
                total += freq // 3 + 1

        return total
        