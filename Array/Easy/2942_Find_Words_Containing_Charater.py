class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:

        # create an empty list to add word indices
        result = []

        # create a loop in which we check each word in order
        for i in range(len(words)):

            # If the string contains characters from the variable x, 
            # then we add the index of this string to the list
            if x in words[i]:
                result.append(i)

        return result