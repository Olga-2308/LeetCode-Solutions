class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        '''
        Since the goal is to score the maximum number of points, 
        letter combinations must be removed in order of point distribution priority. 
        First, remove the letter combinations that give the highest points, and then remove what remains.
        '''

        total = 0
        current1 = []
        current2 = []

        # we consider the first option, when one variable is greater than or equal to the second
        if x >= y: 
            
            # Using a loop, we add characters one by one to an empty array
            for char in s:
                current1.append(char)

                # If the length is greater than or equal to 2, then we can check the substring. 
                # We need to find the characters that give the highest score.
                if len(current1) >= 2:
                    if current1[-2] == "a" and current1[-1] == "b":
                        
                        # add points to the total score
                        total += x

                        # delete the last two characters
                        del current1[-1]
                        del current1[-1]

            # we remove substrings that give fewer points
            for char in current1:
                current2.append(char)
                if len(current2) >= 2:
                    if current2[-2] == "b" and current2[-1] == "a":
                        total += y
                        del current2[-1]
                        del current2[-1]

        # We analyze the second case in the same way
        if y > x:
            for char in s:
                current1.append(char)
                if len(current1) >= 2:
                    if current1[-2] == "b" and current1[-1] == "a":
                        total += y
                        del current1[-1]
                        del current1[-1]
            for char in current1:
                current2.append(char)
                if len(current2) >= 2:
                    if current2[-2] == "a" and current2[-1] == "b":
                        total += x
                        del current2[-1]
                        del current2[-1]

        return total