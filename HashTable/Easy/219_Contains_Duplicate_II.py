class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:


        # If the length of the set of numbers is equal to the length of the array, 
        # then we return false, since if the set has not changed, then there are no duplicates.
        if len(set(nums)) == len(nums):
            return False

        d = {}

        # creates a loop in which we instantly find a duplicate using a dictionary
        for i in range(len(nums)):

            # If the number is not in the dictionary, then the duplicate has not yet been found, 
            # and we write the number into the dictionary
            if nums[i] not in d:
                d[nums[i]] = i
            
            # If the number is already in the dictionary, then the pair of numbers has been found and it remains 
            # to check whether the absolute value of the difference is less than the given number
            else:
                if abs(i - d[nums[i]]) <= k:
                    return True
                
                # If the pair of numbers does not match, then we write the number into the dictionary 
                # and continue the search until the end of the loop
                d[nums[i]] = i

        return False