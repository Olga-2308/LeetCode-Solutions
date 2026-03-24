class Solution:
    def averageValue(self, nums: List[int]) -> int:

        # create an empty list for numbers that meet the conditions of the problem
        numbers = []

        # гsing a loop, we iterate through all the elements of the list and add those that are divisible by 2 and 3 to the new list
        for num in nums:
            if num % 2 == 0 and num % 3 == 0:
                numbers.append(num)

        # ''' If no numbers are found after checking the numbers, an error will occur when searching for the average value. 
        # Therefore, it is necessary to check whether the new list contains elements. If the list is empty, then 0 is returned. '''
        if len(numbers) == 0:
            return 0

        # find the average value from the new list
        result = sum(numbers) // len(numbers)
        
        return result