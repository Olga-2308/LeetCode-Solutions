class Solution:
    def reversePrefix(self, s: str, k: int) -> str:

        # We find two slices formed from the string. 
        # Since K characters are required at the beginning of the string, the slice of the first part is written as [:k]. 
        # In this case, the slice will contain K characters with indices starting with 0.
        part1 = s[:k]
        part2 = s[k:]

        # reverse the first part of the line
        rev = part1[::-1]

        # return the modified string
        return rev + part2 