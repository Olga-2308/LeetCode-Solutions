class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:

        pairs = 0
        remainders = 0
        d = {}

        # We create a dictionary in which we write down the frequency of each number.
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        # Using a loop, we determine the number of pairs and the number of remaining numbers without a pair.
        for val, freq in d.items():

            # To determine how many pairs can be made from identical numbers, 
            # it is necessary to determine the integer division number
            p = freq // 2

            # add the result to the total number of pairs
            pairs += p

            # If the frequency number is odd, this means that one number will always remain without a pair, 
            # and this 1 is added to the number of remaining numbers without a pair.
            if freq % 2 == 1:
                remainders += 1

        return [pairs, remainders]