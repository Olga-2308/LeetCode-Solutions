class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:

        # create a counter to count string
        counter = 0
 
        # create a loop in which we check each element from the list of words
        for word in words:

            # Using this method, we check whether the element is a prefix of the original word; 
            # if so, we increase the counter by 1
            if s.startswith(word):
                counter += 1

        return counter