class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        # create an empty list to create a new list
        result = []

        # find the middle of the list
        middle = len(nums) // 2

        # ''' we create new slices: 
        # the first one is from the beginning of the given list to the middle, 
        # the second one is from the middle of the given list to the end '''
        first = nums[:middle]
        second = nums[middle:]

        # ''' We create a loop in which we work with each element of the list in order, 
        # since the first and second lists are equal, the elements will go through the loop in parallel '''
        for i in range(len(first)):
            f = first[i]
            s = second[i]

            # ''' add the current element from the first part of the list to the list, 
            # then the current element from the second part of the list. '''
            result.append(f)
            result.append(s)

        return result