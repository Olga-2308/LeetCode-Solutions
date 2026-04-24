class Solution:
    def maxPower(self, s: str) -> int:

        # We set counters for the maximum and current values ​​respectively
        power = 1
        counter = 1

        # We compare adjacent characters of a string, counting the number of characters while they are equal
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                counter += 1

                # If the current length of the substring is greater than the maximum, then we update the final counter
                if counter > power:
                    power = counter
            
            # As soon as the line is interrupted, we set the counter to 1 and start counting a new line
            else:
                counter = 1
        
        return power