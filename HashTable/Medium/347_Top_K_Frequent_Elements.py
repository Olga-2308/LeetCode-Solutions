class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = {}
        result = []

        # we determine the frequencies of numbers in an array
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        pairs = []

        # For more convenient sorting, we create an array of pairs of numbers, 
        # where the frequency value is in the first place in the subarray
        for val, freq in d.items():
            pairs.append([freq, val])

        # sort the resulting array in descending order
        pairs.sort(reverse = True)

        # we add to the result the numbers that are under index 1 in each subarray
        for i in range(k):
            result.append(pairs[i][1])

        return result