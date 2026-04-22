class Solution:
    def sortVowels(self, s: str) -> str:
        '''
        You need to return a string in which all the vowels are in the same positions, 
        but their order within the string is in the nondecreasing order. 
        To do this, you need to create a list of all the vowels, sort them, 
        and return them to their positions in the original string.
        '''

        vowels = "aeiouAEIOU"
        vowel = []

        # Create a separate list of vowels
        for char in s:
            if char in vowels:
                vowel.append(char)

        vowel.sort()

        # create a variable that will indicate the vowel index when replacing characters
        indx = 0

        result = []

        # replace the vowels of the original string with vowels from the sorted array
        for char in s:
            if char in vowels:
                result.append(vowel[indx])
                indx += 1
            else:
                result.append(char)
            
        # return the string as specified in the problem statement
        return "".join(result)