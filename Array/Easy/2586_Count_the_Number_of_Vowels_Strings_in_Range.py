class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:

        # We create a string with vowels that must be at the beginning and end of a word to fulfill the condition of the problem.
        vowels = 'aeiou'

        # We create a counter for matching words.
        counter = 0

        # Since words within a specific index range are needed, these restrictions can be specified directly in the loop itself. 
        # We add one to the right side so the value isn't included.
        for i in range(left, right + 1):

            # We need to determine whether the first and last characters of a word are vowels. 
            # We create a variable and assign it the value of the current word, 
            # then check the first and last characters at indexes 0 and -1, respectively. 
            # If both characters are vowels, we increment the counter by 1.
            word = words[i]
            if word[0] in vowels and word[-1] in vowels:
                counter += 1

        return counter