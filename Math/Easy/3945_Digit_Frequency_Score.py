class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        '''
        To find the product of the digits of a number and their quantity, 
        you just need to find the sum of all the digits 
        --- 112233 => 1 + 1 + 2 + 2 + 3 + 3 = (1 * 2) + (2 * 2) + (3 * 2) = 12 ---
        '''

        total = 0

        # Using a loop, we add the digits of a number one by one 
        # (before this, we convert the string symbol into a number)
        for char in str(n):
            total += int(char)

        return total

        '''
        d = {}
        total = 0

        for char in str(n):
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1

        for char, freq in d.items():
            total += int(char) * freq

        return total
        '''