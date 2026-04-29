class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        d = {}
        total = 0
        result = []

        # take pairs of numbers with the same indices from two arrays one after the other.
        for i in range(len(A)):

            # If the symbol is not in the dictionary, we add it and indicate the quantity
            if A[i] not in d:
                d[A[i]] = 1
            
            # If the symbol already existed, then we increase the counter
            else:
                d[A[i]] += 1

                # If the value (number of repetitions) is equal to two, 
                # then we have collected the same pair of numbers and therefore increase the total pair counter by 1
                if d[A[i]] == 2:
                    total += 1

            # We check each character from the second array in the same way.
            if B[i] not in d:
                d[B[i]] = 1
            else:
                d[B[i]] += 1
                if d[B[i]] == 2:
                    total += 1

            result.append(total)

        return result