class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
    
        # We create a set into which we will add all the average values, 
        # where ultimately only unique values ​​without duplicates will be stored
        average_pairs = set()

        # We sort the array so that we take the minimum values ​​on one side and the maximum values ​​on the other, 
        # as required by the problem statement.
        nums.sort()

        # we set pointers at different ends of the array
        i = 0
        j = len(nums) - 1


        while i < j:

            # add the mean value to the set
            average_pairs.add((nums[i] + nums[j]) / 2)

            # we shift the pointers by one towards the center of the next pair of numbers
            i += 1
            j -= 1

        return len(average_pairs)