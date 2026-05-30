class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        '''
        The problem statement states that duplicates occur twice. Therefore, 
        it is necessary to somehow mark each number so that when a duplicate is found, 
        it is clear that the same number has previously appeared in the array and the current one is a duplicate. 
        Since duplicates are identical, their values ​​can be used as identical marks or addresses. 
        Each unique number refers to a unique index in the array (by subtracting 1 from the number). 
        Since indexes are unique in the array, each unique number will refer to a unique index, 
        which is found based on the number's unique value. And if there are duplicates in the array, 
        they will all refer to the same number at the same index. 
        It is necessary to somehow mark the numbers found at the indexes each time. 
        The simplest way is to turn the number at the index into a negative number. 
        If the value is positive when the number at the address is first accessed, 
        then this is the first time and the current number is not a duplicate. 
        If we navigate to an address and see a negative number, 
        it means that the exact same number was there before 
        and turned the value at the address into a negative number. 
        This is our duplicate.
        '''

        result = []

        # Using a loop, we check each number in the array. 
        # First, we determine the index by which we will access another number to identify duplicates. 
        # We take the number by its module, since it may be that the previous 
        # values ​​of the array have previously accessed this number
        for i in range(len(nums)):
            indx = abs(nums[i]) - 1

            # If the number at the address is less than 0, 
            # this means that there was exactly the same number here before 
            # and it turned the number at the address into a negative number, 
            # and at the current iteration of the loop we have a duplicate and we add its modulus to the result
            if nums[indx] < 0:
                result.append(abs(nums[i]))
            
            # If the number is greater than 0, it means we are here for the first time and the number is not a duplicate, 
            # but to mark that we were here (there is a possible duplicate), 
            # we turn the number at the address into a negative number
            else:
                nums[indx] *= (-1)

        return result

        '''
        d = {}
        result = []

        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                result.append(num)

        return result
        '''