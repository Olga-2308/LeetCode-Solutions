class Solution:
    def smallestEqual(self, nums: List[int]) -> int:

        # since we need to return the minimum suitable index, 
        # the index of the first number that satisfies all the conditions will be returned
        for i in range(len(nums)):

            # If the index, when divided by 10, yields a remainder equal to the value of the number under that index, 
            # then we immediately return that index and end the loop
            if i % 10 == nums[i]:
                return i
            
        # If after checking all numbers such an index is not found, then we return -1
        return -1