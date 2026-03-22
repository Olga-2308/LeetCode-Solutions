class Solution:
    def countKeyChanges(self, s: str) -> int:
        # create a counter that will show the number of changes
        counter = 0

        # ''' the condition states that 'a' == 'A', 
        # but in the code these characters are not equal, therefore, 
        # it is necessary to convert the characters to lowercase so that the condition of the task is satisfied '''
        s_low = s.lower()

        # ''' We compare two adjacent symbols; if they are not equal, then we add 1 to the counter 
        # (!) in order not to go beyond the limit when comparing the last character, 
        # it is necessary to subtract 1 from the length '''
        for i in range(len(s)-1):
            # We compare two adjacent symbols with each other. If they are not equal, then increase the counter by 1
            if s_low[i] != s_low[i+1]:
                counter += 1

        return counter
        