class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        '''
        To solve this problem, we first need to sort the array. 
        Adjacent numbers produce the smallest possible difference. 
        Therefore, we first determine the absolute minimum value, 
        and then check pairs of adjacent numbers whose absolute difference equals the found value.
        '''

        arr.sort()
        result = []
        min_value =  float('inf')

        # we find the minimum difference between the numbers
        for i in range(len(arr) - 1):
            if abs(arr[i] - arr[i+1]) < min_value:
                min_value = abs(arr[i] - arr[i+1])

        # we find and count pairs of numbers that meet the conditions 
        # and their absolute difference is equal to the minimum value found
        for i in range(len(arr) - 1):
            if abs(arr[i] - arr[i+1]) == min_value:
                result.append([arr[i], arr[i+1]])

        return result