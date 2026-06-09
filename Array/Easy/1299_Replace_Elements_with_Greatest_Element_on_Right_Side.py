class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        '''
        When moving forward in the loop, 
        each maximum value must be calculated from the entire array, 
        but if you go the other way, then at the first iteration, 
        the current number will be guaranteed to be the maximum, 
        and at each subsequent iteration, you must determine the maximum from only two values ​​- 
        the current number in the loop and the maximum value that was found earlier.
        '''

        res = []
        max_num = -1

        # Using a loop, we find the maximum values ​​from the end 
            # (-1 of the array length - to avoid going beyond the loop boundary, 
            # 0 - we end the loop at index zero so as not to check the last element, since it is always equal to -1, 
            # -1 - we step in the opposite direction)
        for i in range(len(arr) - 1, 0, -1):

            # We determine the maximum value and add it to the final array.
            max_num = max(max_num, arr[i])
            res.append(max_num)

        # We reverse the array so that the maximum values ​
        # ​for each subarray are in direct order 
        # and add the last element -1 
        # (the first one in reverse order that was skipped)
        result = res[::-1]
        result.append(-1)

        return result


        '''
        res = []
        d = {}
        max_num = -1

        for i in range(len(arr) - 1, -1, -1):
            max_num = max(max_num, arr[i])
            d[i] = max(max_num, arr[i])

        for indx, maxi in d.items():
            if indx == 0:
                continue
            else:
                res.append(maxi)

        result = res[::-1]
        result.append(-1)

        return result
        '''