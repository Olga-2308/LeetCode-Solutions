class Solution:
    def reverseVowels(self, s: str) -> str:
        
        '''
        Create a list of vowels and an empty array to search for characters in a given string.
        '''
        vow_alp = 'aeiouAEIOU'
        vowels = []

        '''
        Using a loop, we find all the vowels in the string and add them to the prepared array.
        '''
        for char in s:
            if char in vow_alp:
                vowels.append(char)

        '''
        Reversing the array to put the vowels back in the correct order
        '''
        revers = vowels[::-1]

        '''
        We create a list of the new sequence of all symbols and 
        a variable with the value 0 to insert each vowel from the new array one by one.
        '''
        result = []
        indx = 0

        '''
        We create a loop in which we search for vowels and replace them with vowels from the array. 
        To ensure each vowel is in its proper place, we increment the index by 1 each time.
        '''
        for char in s:
            if char in vow_alp:
                result.append(revers[indx])
                indx += 1
            else:
                result.append(char)

        '''
        return the string as required in the problem statement.
        '''
        return ''.join(result) 