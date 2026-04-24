class Solution:
    def generateTag(self, caption: str) -> str:

        # each line will start with this character, so we write it at the beginning of the final string
        result = "#"

        # turn the string into an array of strings to work with each string individually and remove extra spaces.
        cap = caption.split()

        for i in range(len(cap)):

            # create a loop and add each converted word to the resulting string. 
            # add the first word separately, as it needs to be returned in its entirety in lowercase.
            if i == 0:
                word = cap[i].lower()
                result += word
            
            # add the remaining words to the line, having first converted them into words with the first capital letter
            else:
                word = cap[i].title()
                result += word

        # Return the string truncated to 100 characters
        return result[:100]