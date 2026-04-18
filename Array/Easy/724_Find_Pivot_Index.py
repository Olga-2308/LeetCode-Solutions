class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        # We find the total sum with which we will search for the term
        total_sum = sum(nums)
        left_sum = 0

        # We create a loop in which we check the right and left sums excluding the current number, 
        # if the sums are equal then the number is found
        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]
            if left_sum == right_sum:
                return i
            
            # If the current number is not suitable, then we add it to the left sum for the following comparisons
            else:
                left_sum += nums[i]

        # If a pivot number is not found, then we return -1
        return -1