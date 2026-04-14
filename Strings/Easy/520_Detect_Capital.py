class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        # To determine whether a word matches one of the rules, 
        # we need to create reference samples that exactly match one of the conditions. 
        # For this, we use string methods: 
            # 1) The first letter is capitalized, the rest are lowercase. 
            # 2) All letters in the word are capitalized. 
            # 3) All letters are lowercase.
        cap = word.capitalize()
        low = word.lower()
        up = word.upper()

        # If a word from the problem statement matches at least one of the generated reference words, 
        # then we return true, otherwise false
        return word == cap or word == low or word == up