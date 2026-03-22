class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # turn a string into a list of strings
        lst_s = s.split()

        # ''' remove list elements from k to the end of the list. 
        # start deleting a list with k element, since element indices start from 0. 
        # for example, if we need to leave 4 elements of the list (k = 4), 
        # then elements with indices 0, 1, 2, 3 remain in the list, and elements with k = 4 to the end of the list will be deleted '''
        del lst_s[k::]

        # turn the list back into a string using the method .join()
        result = " ".join(lst_s)

        return result