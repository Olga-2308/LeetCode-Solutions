class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        '''
        We need to determine a number that takes up more than 25 percent of the space in the array. 
        After determining the array length, we calculate the number of elements that take up 25 percent. 
        Using a loop, we count the number in the array and return that number as soon as the number exceeds 25 percent.
        '''

        # We determine the minimum number of identical numbers that must be in the array.
        l = len(arr)
        part = l / 4

        # In a loop, we count the number of times each element is repeated. 
        # Once the number exceeds 25 percent, we return the current number.
        for num in arr:
            if arr.count(num) > part:
                return num