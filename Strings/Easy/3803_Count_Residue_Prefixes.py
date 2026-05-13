class Solution:
    def residuePrefixes(self, s: str) -> int:

        counter = 0
        prefix = ""

        # Using a loop, we add characters one by one, creating new prefixes
        for char in s:
            prefix += char

            # We check each prefix to see if the problem condition is met. 
            # If the number of unique characters in the prefix equals the length of the remaining prefix, 
            # then we increment the counter.
            if len(set(prefix)) == len(prefix) % 3:
                counter += 1

        return counter