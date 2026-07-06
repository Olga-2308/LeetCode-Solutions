class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''
        Given a two-dimensional array, each number in the array has two adjacent links to numbers in the next (lower) array. 
        To find the shortest path, it is necessary to determine the shortest paths 
        from the previous to the current subarray in each subarray.
        '''
        
        # If a two-dimensional array is given one subarray, 
        # then we can immediately determine the shortest path by finding the minimum value of the subarray
        if len(triangle) == 1:
            return min(triangle[0])

        # We create an array to store the current minimum path values. 
        # Since this is a two-dimensional array and the path length is determined between 
        # the current and next subarrays, all previously traversed subarrays are not included in the path search. 
        # Therefore, we can create a one-dimensional array that will overwrite the updated current subarray 
        # with all possible paths each time.
        dp = triangle[0]

        # using a loop we find all the minimal paths that can be used to reach the next subarray
        for i in range(1, len(triangle)):

            # create an array to count the current minimum paths
            current = []

            # Next, using a nested loop, we find the minimum path for each number in the current subarray
            for j in range(len(triangle[i])):
                min_way = float('inf')

                # A number has two options for descending: to the right or to the left. 
                # First, we need to determine whether the current number is the outermost element in its subarray. 
                # If not, its path also goes along the left side, and we can determine it. 
                # To do this, we find the minimum value between the current variable 
                # (it may have been found previously, so we need to find the minimum each time) and the new path. 
                # The new path is defined as the current value of the number and its left-hand neighbor from the dynamic array, 
                # which was found previously. Since the current element is not the outermost element in its subarray, 
                # it has a path to the left.
                if j > 0:
                    min_way = min(min_way, triangle[i][j] + dp[j - 1])

                # We also determine the sum with the right element in the same way, if it exists. 
                # It exists if the length of the dynamic array is greater than the current position of the current element.
                if j < len(dp):
                    min_way = min(min_way, triangle[i][j] + dp[j])

                # We add the found minimum sum to the current array. 
                # After the current nested loop completes, the current array will become a new dynamic array, 
                # and the search for further minimum values ​​will proceed from there.
                current.append(min_way)
            
            # After we have calculated all possible minimal paths of the current subarray, 
            # we define this array as dynamic and at the next iteration all minimal paths will be 
            # found based on the values ​​of this array
            dp = current

        return min(dp)