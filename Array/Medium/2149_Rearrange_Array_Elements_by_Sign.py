class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        positive = []
        negative = []

        # Distribute positive and negative numbers into two arrays
        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negative.append(num)

        result = []

        # We create a final array in which the sequence of numbers corresponds to the conditions of the problem
        for i in range(len(positive)):
            result.append(positive[i])
            result.append(negative[i])

        return result