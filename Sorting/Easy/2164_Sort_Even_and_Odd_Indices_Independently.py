class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:

        '''
        To obtain the required array, you need to divide the elements of the original list into even and odd groups. 
        Then sort each array as specified in the condition. 
        After that, return the array elements in the new, correct order. 
        Finally, check whether the last element is left outside the loop, and if so, append it to the end of the resulting array.
        '''

        odd = []
        even = []

        # We distribute the numbers of the array into two new lists
        for i in range(len(nums)):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])

        # We sort the resulting lists in ascending and descending order, respectively.
        odd.sort(reverse = True)
        even.sort()

        result = []

        # We add numbers from two sorted arrays one by one to the final list.
        for i in range(len(odd)):
            result.append(even[i])
            result.append(odd[i])

        # If one of the arrays is one element larger than the other, 
        # then we use the check to determine the ratio of the lengths and add the last element from the list.
        if len(even) > len(odd):
            result.append(even[-1])

        return result