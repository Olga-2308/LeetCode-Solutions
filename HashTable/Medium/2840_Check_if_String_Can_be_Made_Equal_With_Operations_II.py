class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        '''
        To determine whether it's possible to create a string equal to another using permutations, 
        you need to know which characters are at even and odd indexes in the dictionaries. 
        This is because you can only select indexes where their difference is an even number. 
        This is possible if the pair contains only even indexes or only odd indexes. 
        Therefore, pairwise permutations are only possible between even indexes and between odd indexes.
        '''

        s1_even = {}
        s1_odd = {}

        s2_even = {}
        s2_odd = {}

        # Determine the frequency of characters in the indexes and distribute them among the corresponding dictionaries
        for i in range(len(s1)):
            if i % 2 == 0:
                if s1[i] not in s1_even:
                    s1_even[s1[i]] = 1
                else:
                    s1_even[s1[i]] += 1
            else:
                if s1[i] not in s1_odd:
                    s1_odd[s1[i]] = 1
                else:
                    s1_odd[s1[i]] += 1

        # We analyze the second line in the same way.
        for i in range(len(s2)):
            if i % 2 == 0:
                if s2[i] not in s2_even:
                    s2_even[s2[i]] = 1
                else:
                    s2_even[s2[i]] += 1
            else:
                if s2[i] not in s2_odd:
                    s2_odd[s2[i]] = 1
                else:
                    s2_odd[s2[i]] += 1

        # If pairs in a dictionary are equal to each other, 
        # then one string can be converted into a string equal to the other using permutations
        return s1_even == s2_even and s1_odd == s2_odd