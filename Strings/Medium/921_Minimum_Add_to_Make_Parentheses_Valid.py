class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        '''
        There are two cases when parenthesis counters will increment: 
        when an opening parenthesis lacks a closing parenthesis, 
        and when a closing parenthesis can no longer be paired with an opening parenthesis 
        because all subsequent opening parentheses are invalid.
        '''

        open_b = 0
        close_b = 0

        # we start checking each bracket using a loop
        for char in s:

            # If the parenthesis is an opening parenthesis, 
            # then we increment the counter and wait until a valid pair appears for it.
            if char == "(":
                open_b += 1

            # If the bracket is closing, then there are two options
            else:

                # If opening parentheses were previously added to the line, 
                # then this closing parenthesis will be a pair for one of the opening ones, 
                # so we don’t take the closing parenthesis into account anywhere 
                # and at the same time we decrease the counter of opening parentheses by 1, 
                # since a pair was found for one of them
                if open_b > 0:
                    open_b -= 1

                # If we have a closing parenthesis and there were no opening parentheses (open_b < 0) before, 
                # this means that this closing parenthesis will no longer be able to find a valid pair, 
                # since any entry of the form )(((... is not valid
                else:
                    close_b += 1

        return open_b + close_b