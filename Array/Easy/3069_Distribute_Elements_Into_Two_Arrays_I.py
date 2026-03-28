class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:

        # Create two empty lists and add one element to each, as specified in the problem statement. 
        # Add the first element of the original array to the first list, 
        # and add the second element of the original array to the second list.
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        # create a loop in which we distribute the remaining elements of the original array. 
        # begin the loop with the third element at index 2. 
        # The first element at index 0 and the second element at index 1 are already distributed among the created lists.
        for i in range(2, len(nums)):

            # If the last value of the first list is greater than the last value of the second list, 
            # then the current number is added to the first array.
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])

            # otherwise we add the number to the second list
            else:
                arr2.append(nums[i])

        # combine the two resulting arrays of numbers
        result = arr1 + arr2

        return result