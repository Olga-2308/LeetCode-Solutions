class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        '''
        To obtain the maximum sum of all found medians, 
        it is necessary to distribute the largest values ​​evenly among all triples of numbers. 
        To do this, sort the array, identify the triples of numbers, 
        and return the sum of the medians from each triplet.
        '''

        # sort the array in ascending order
        nums.sort()

        # since the length of the array is divisible by 3, 
        # we can determine how many triplets we can make
        part = len(nums) // 3
        result = 0

        # Since the smallest values ​​are at the beginning of the sorted array, 
        # we distribute them evenly among all triplets. 
        # Since they are minimal, they are not the median in each triplet.

        # we create an array of numbers in which we need to distribute pairs of numbers into the remaining places in the triplets
        main = nums[part:]

        # since pairs of numbers will be added successively to each triplet, 
        # then in each of these pairs, the minimum number is the median of the triplet
        for i in range(0, len(main), 2):

            # we find the sum of all the numbers on even indices, 
            # since these numbers are the medians of each of the triplets
            result += main[i]

        return result