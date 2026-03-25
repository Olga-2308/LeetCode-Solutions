class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:

        # we create an empty list to which list elements will be added
        result = []

        # we create a loop in which we work with the list elements one by one
        for word in words:

            # replace the separator with a space
            res = word.replace(separator, ' ')

            # converting a string into a list
            new_res = res.split()

            # add list items to a new list
            result.extend(new_res)

        return result
            