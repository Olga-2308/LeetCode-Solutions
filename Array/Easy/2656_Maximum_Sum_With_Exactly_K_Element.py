class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:

        #create an empty list for the found numbers
        result = []

        # create a loop in which the code is executed until the number of steps (k) becomes equal to 0
        while k != 0:

            # We are looking for the maximum number in the list.
            n = max(nums)

            # add it to the final list
            result.append(n)

            # find the index of this maximum number
            indx = nums.index(n)

            # and increase this number by 1
            nums[indx] += 1

            # reduce the number of moves by 1 to avoid getting stuck in an infinite loop.
            k -= 1 
            
        # return the sum of numbers
        return sum(result)