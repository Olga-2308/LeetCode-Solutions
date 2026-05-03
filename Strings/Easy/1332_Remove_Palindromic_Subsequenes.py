class Solution:
    def removePalindromeSub(self, s: str) -> int:
        '''
        If the string is already a palindrome, then only one step is required to make the string empty. 
        
        If the string is not a palindrome, then in one step you can remove all the letters "a" or all the letters "b", 
        and then the remaining letters will be a palindrome in any case, and in a second step, the string becomes empty.
        '''

        if s == s[::-1]:
            return 1
        else:
            return 2