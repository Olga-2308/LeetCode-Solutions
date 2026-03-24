class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:

        # we create a variable in which the maximum result will be written
        max_count = 0

        # we create a loop in which we access each element of the list
        for s in sentences:
            # split a string (list element) into a list of words
            sp = s.split(' ')
            # we count the number of these words
            count = len(sp)
            # If the number is greater than the one written in the variable, then we replace it with the one just found
            if count > max_count:
                max_count = count

        return max_count
        