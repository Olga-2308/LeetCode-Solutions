class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        '''
        To return the minimum number of deletions, 
        you need to determine the frequency of each character in the string 
        and then delete all characters with the minimum frequency until the number of unique characters equals k
        '''

        d = {}
        counter = 0

        # Using a dictionary, find the frequency of each character in a string
        for char in s:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1

        # If the dictionary length is less than or equal to the value k, 
        # then there are already fewer and sufficient unique letters and nothing needs to be deleted.
        if len(d) <= k:
            return 0

        f = []

        # We create an array with all the frequency values, 
        # one element indicates how many identical letters can be removed
        for freq in d.values():
            f.append(freq)

        # We sort the resulting array in reverse order so 
        # that the minimum values ​​are at the end and can be easily removed.
        f.sort(reverse = True)

        # It is necessary to delete letters until the number of unique letters equals k. 
        # We delete the letters with the minimum frequency one by one 
        # and record the number of deleted characters in the general counter.
        while len(f) > k:
            counter += f[-1]
            del f[-1]

        return counter