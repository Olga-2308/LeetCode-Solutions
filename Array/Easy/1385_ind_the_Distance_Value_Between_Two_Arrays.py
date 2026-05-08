class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        result = 0

        for num in arr1:
            counter = 0

            # We find the absolute difference between elements of two arrays
            for i in range(len(arr2)):

                # If the difference modulus is less than or equal to d, 
                # then we increase the current counter
                if abs(num - arr2[i]) <= d:
                    counter += 1

            # If the counter has not increased during the check and is equal to 0, 
            # then the number from the first array is suitable
            if counter == 0:
                result += 1
    
        return result