class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:

        # find the maximum and minimum values ​​in the list to determine which numbers we definitely cannot return as an answer.
        max_num = max(nums)
        min_num = min(nums)

        # create a loop in which we look for a number that is neither maximum nor minimum
        for num in nums:

            # as soon as we find the first of such numbers, we return it and end the loop
            if num != max_num and num != min_num:
                return num
            
        # If after going through the entire loop, no such numbers were found, 
        # then there is either one number in the list or two - and we return -1
        else:
            return -1