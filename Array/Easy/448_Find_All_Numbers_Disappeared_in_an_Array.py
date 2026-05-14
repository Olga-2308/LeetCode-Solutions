class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # Converting an array to a set of numbers to speed up searching and remove duplicates
        num = set(nums)
        result = []

        # using a loop we check all numbers from 1 to n (inclusive, so we increase by 1)
        for i in range(1, len(nums) + 1):

            # If the number is not in the set, then we add it to the final array
            if i not in num:
                result.append(i)

        return result