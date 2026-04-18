class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        '''
        We create a loop in which we compare each character in turn with the given one. 
        As soon as we find a character that is greater than the given one, we return that character.
        '''
        for char in letters:
            if ord(char) > ord(target):
                return char

        '''
        If such characters are not found in the array, then we return the first element of the array.
        '''
        return letters[0]