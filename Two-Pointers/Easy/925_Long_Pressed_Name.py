class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        i = 0
        j = 0

        # the loop runs until the entire printed line (the second one) is checked
        while j < len(typed):

            # If the name is not yet fully checked and the characters are equal, 
            # then we move both pointers one step forward and continue checking
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1

            # After the same characters in both lines have been shifted, 
            # it is necessary to skip all duplicate characters in the printed text, 
            # if any, so we shift the second pointer until we have passed all the duplicates
            elif j > 0 and typed[j] == typed[j-1]:
                j += 1

            # If the characters in both lines don't match and there is no sticky keys in the second line, then we return false
            else:
                return False

        # If the first pointer reaches the end of the name, 
        # it means that all characters have been printed in the second line and we return true, 
        # otherwise - false
        return i == len(name)