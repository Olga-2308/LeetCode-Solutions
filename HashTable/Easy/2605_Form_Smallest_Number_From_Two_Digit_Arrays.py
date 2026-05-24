class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        There can be two possible answers: if a digit appears in both arrays, then we return the minimum intersection; 
        otherwise, we find the minimum values ​​in each array and create the minimum number from two digits.
        '''

        min_digit1 = float('inf')
        min_digit2 = float('inf')
        d = {}

        # we determine the frequency of each number from both arrays
        for num in nums1:
            min_digit1 = min(num, min_digit1)

            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        for num in nums2:
            min_digit2 = min(num, min_digit2)

            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        result = float('inf')

        # If the frequency of a number is greater than 1, it means that the number is in both arrays, 
        # since the numbers in each array are unique.
        for num, freq in d.items():
            if freq > 1:
                result = min(result, num)

        # If such a number was found, then we return it
        if result < 10:
            return result
        
        # If the number is not found, then we make up the minimum number 
        # from the two minimum values ​​found from each array
        else:
            if min_digit1 < min_digit2:
                return int(str(min_digit1) + str(min_digit2))
            else:
                return int(str(min_digit2) + str(min_digit1))