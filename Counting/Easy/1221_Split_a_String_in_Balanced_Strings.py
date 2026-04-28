class Solution:
    def balancedStringSplit(self, s: str) -> int:

        counter_R = 0
        counter_L = 0

        total = 0

        # We create a loop in which we search for balanced substrings
        for char in s:
            # The found string is considered balanced as soon as the letter counters become equal.
            if char == "R":
                counter_R += 1

                # Once the letter counters are equal, we've found a balanced string. 
                # We add one to the overall counter and reset the letter counters to zero for further substring searching.
                if counter_L == counter_R:
                    total += 1
                    counter_R = 0
                    counter_L = 0

            # We follow exactly the same logic if we encounter another letter. 
            # Resetting the counters is necessary in any case, as soon as we reach the substring's balance.
            elif char == "L":
                counter_L += 1

                if counter_L == counter_R:
                    total += 1
                    counter_R = 0
                    counter_L = 0

        return total