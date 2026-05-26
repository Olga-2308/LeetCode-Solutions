class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        # We convert the string into a set to remove duplicates and reduce the number of checks.
        symbols = set(word)
        counter = 0

        # we check each character in the string
        for char in symbols:

            # If a letter is in the set in both upper and lower case, 
            # then the symbol is considered unique and we add it to the counter
            if char.islower() and char.upper() in symbols:
                counter += 1

        return counter

        '''
        D = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
        d = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
        words = set(word)

        for char in words:
            if char in d:
                d[char] += 1
            elif char in D:
                D[char] += 1

        A = []
        a = []
        counter = 0

        for freq in d.values():
            if freq > 0:
                a.append(1)
            else:
                a.append(0)

        for freq in D.values():
            if freq > 0:
                A.append(1)
            else:
                A.append(0)

        for i in range(len(a)):
            if a[i] > 0 and A[i] > 0:
                counter += 1

        return counter
        '''