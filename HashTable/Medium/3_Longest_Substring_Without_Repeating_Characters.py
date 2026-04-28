class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        d = {}
        left = 0
        max_len = 0
        current_len = 0

        # We create a loop in which we go through each character of the string
        for i in range(len(s)):

            # First, we check whether the character is in the dictionary 
            # and whether it is greater than our left substring boundary 
            # (if the character is not in the dictionary, 
            # it is unique and is simply added to the substring; 
            # if its last index in the dictionary is less than the left boundary, 
            # it means the character is outside the substring, which also doesn't satisfy our condition). 
            # Therefore, when we encounter a character that is already in the dictionary and is in our current substring, 
            # it means we've encountered a duplicate and the unique substring is broken.
            if s[i] in d and d[s[i]] >= left:

                # Since the string has been interrupted, we need to start composing a new string. 
                # To do this, we need to determine a new value for the left boundary where the new substring will begin. 
                # Since we currently know where the two duplicates are, one of them (the one to the left) needs to be removed. 
                # To do this, we shift our new boundary one step to the right of the duplicate. 
                # Now, in our new substring, the current duplicate has become a unique character, 
                # and we can continue searching for the maximum substring length.
                left = d[s[i]] + 1

            # It is also necessary to update the indices of each symbol so that in case of repetitions the left border is shifted to the correct (last current) index
            d[s[i]] = i

            # and each time we calculate the current length of the substring, 
            # for this we subtract the index of the left border from the current index 
            # (it is always larger, since it determines the right boundary of the substring at the current moment)
            current_len = i - left + 1

            # We determine the maximum length
            if current_len > max_len:
                max_len = current_len

        return max_len