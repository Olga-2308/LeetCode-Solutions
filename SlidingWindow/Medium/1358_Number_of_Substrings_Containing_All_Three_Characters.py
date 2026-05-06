class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        counter = 0

        # We'll create a dictionary in which we'll record the last indexes of the letters encountered. 
        # Initially, we'll assign each letter a value of -1, since string indexing starts at 0.
        indx = {'a': -1, 'b': -1, 'c':-1}

        #
        for i in range(len(s)):

            # If the character a, b, or c is encountered during the iteration, 
            # we update the dictionary index. 
            # Even if we continually update the index of the same letter, 
            # if one of them still has a value of -1, the substring is considered invalid, 
            # and we continue searching for all the letters.
            indx[s[i]] = i

            # As soon as all -1 values ​​have disappeared from the dictionary, 
            # this means that we have found the first substring where all 3 characters appear
            if -1 not in indx.values():

                # If the string doesn't contain -1, then we have a suitable substring and need to determine how many can be created. 
                # To do this, we need to determine the minimum index in the dictionary—this is the minimum value 
                # that must be in the substring for all three letters to be in that substring. For example, if the minimum index is 0, 
                # this means we can create only one substring in the current loop iteration. But since indexing starts at 0, 
                # and there is only one possible string, we need to add 1 to the index—this result will be the number of possible substrings. 
                # (For example, with a minimum index of 1, it is possible to create two substrings in the current loop iteration. 
                # The first substring starts at index 0, and the second string starts at index 1.
                # Therefore, we add 1 to the current minimum index (1 + 1 = 2)). 
                # After we've counted all possible substrings in the current loop iteration, we add the next character to the substring, 
                # update the dictionary indices, and count the number of new substrings. 
                # If the minimum index hasn't changed, then the number of substrings in the current iteration 
                # is equal to the number of substrings in the previous iteration (we simply added another character at the end, 
                # resulting in a new string, which also needs to be counted). 
                # If the minimum value has changed, then we determine the new number of substrings by adding 1 to the minimum value. 
                # This way, we reach the end of the loop, counting all valid substrings each time.
                counter += min(indx.values()) + 1

                # s = "abcabc"

                # i = 0
                # [a] At this iteration, we have 1 character in the string, 
                # so we update the value in the dictionary: indx = {'a': 0, 'b': -1, 'c':-1}

                # We updated the indexes and the dictionary still has -1, 
                # which means the current substring is not suitable for us.
                

                # i = 1
                # [ab] At this iteration, we have 2 character in the string,
                # so we update the value in the dictionary: indx = {'a': 0, 'b': 1, 'c':-1}

                # We updated the indexes and the dictionary still has -1, 
                # which means the current substring is not suitable for us.
            

                # i = 2
                # [abc] At this iteration, we have 3 character in the string,
                # so we update the value in the dictionary: indx = {'a': 0, 'b': 1, 'c':2}
                
                # All -1 values ​​have disappeared from the dictionary, 
                # meaning that the current substring contains at least one of the required characters.
                # Now we need to determine how many substrings we can create at the current stage of the loop, 
                # where i (the end of the substring) is equal to 2.
                # For the string to contain all characters, we need the minimum substring to contain the furthest character
                # (the furthest character from u is the character with the minimum index, 
                # and the rest of the characters are located between them)

                # This means that the minimum possible string contains characters 
                # from index 0 to the current index in the loop (i)
                # The minimum index in the dictionary is 0, the current index is 2. 
                # Therefore, the substring contains elements at indexes 0, 1, 2 -- >

                # Here we have determined the minimum possible string, but the string can be larger,
                # if there are additional indices on the left side after the minimum.
                # But in this case, our minimum index is 0.
                # It turns out there can't be any characters before it, so we can only create one substring.
                # But since a real string is taken as 1, and indexing starts at 0,
                # then 1 is added to the minimum index (0 + 1 = 1).
                # It turns out that in this iteration, we can only create one substring [abc]

                # (1) Minimum possible string: [abc]
                # Additional string: -
                

                # i = 3
                # [abca] At this iteration, we have 4 character in the string,
                # so we update the value in the dictionary: indx = {'a': 3, 'b': 1, 'c':2}
                
                # The smallest possible string contains indices 1, 2, 3 --> [bca]
                # Now we need to determine how many additional substrings can be formed using the characters
                # that appear before (to the left) the minimum index. The minimum index is 1,
                # therefore, there is only one character at index 0 that can form a new substring.

                # (2) Minimum possible string: [bca]
                # (3) Additional string: a[bca]

                # We were able to form 2 strings on the current loop iteration.
                # The formula yields: 1 (minimum index) + 1 = 2
                
                
                # i = 4
                # [abcab] At this iteration, we have 5 character in the string,
                # so we update the value in the dictionary: indx = {'a': 3, 'b': 4, 'c':2}

                # (4) Minimum possible string: [cab]
                # (5) Additional string: b[cab]
                # (6) Additional string: ab[cab]
                
                
                # i = 5
                # [abcabc] At this iteration, we have 6 character in the string,
                # so we update the value in the dictionary: indx = {'a': 3, 'b': 4, 'c':5}

                # (7) Minimum possible string: [abc]
                # (8) Additional string: c[abc]
                # (9) Additional string: bc[abc]
                # (10) Additional string: abc[abc]

        return counter